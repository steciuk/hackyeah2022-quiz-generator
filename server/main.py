from typing import Union
from urllib.parse import urlencode, urljoin

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.responses import Response
from pydantic.main import BaseModel

from generator import generateQuestions
from quizPdfBuilder import QuizPdfBuilder

# TODO
# Remove whitespace from models
#
# generate PDF

app = FastAPI()


class GeneratePdfQuizRequest(BaseModel):
    sourceUrl: str
    title: str


class Article:
    url: str
    title: str
    description: str

    def __init__(self, url: str, title: str, description: str):
        self.url = url
        self.title = title
        self.description = description


@app.post("/generate")
def generateQuiz(req: GeneratePdfQuizRequest):
    text = None

    if req.sourceUrl.endswith(".pdf"):
        print("implement PDF")
    else:
        text = queryIPNSourceFromWebsite(req.sourceUrl)

    generatedQuestions = generateQuestions(text)

    pdfPath = f'static/ipn_quiz.pdf'

    pdf = QuizPdfBuilder()
    pdf.add_page()
    pdf.addTitle(req.title)
    for question in generatedQuestions:
        pdf.addQuestionTitle(question.question)
        pdf.addQuestionAnswers(question)

    output = pdf.output(pdfPath, 'S')
    response = Response(
        content=output,
        media_type="application/pdf",
        headers={
            'Content-Disposition': 'attachment; filename="ipn-quiz.pdf"'
        })
    return response


@app.get("/search/{query}")
def searchIPNArticles(query: str, q: Union[str, None] = None) -> list[Article]:
    request_url: str = RequestBuilder(query).build()
    response = requests.get(request_url)
    searchResults = parseIPNResults(response)
    return searchResults


def queryIPNSourceFromWebsite(url: str) -> str:
    # add try catch
    # detect if language is english
    # detect if any content can be used -> not empty text, not weird content images etc
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    all_paragraphs = soup.find_all('p')
    all_paragraphs_texts: list[str] = []
    for p in all_paragraphs:
        paragraph = p.getText().strip()
        if paragraph:
            all_paragraphs_texts.append(paragraph)

    return '\n'.join(all_paragraphs_texts)


class RequestBuilder:
    url = "https://szukaj.ipn.gov.pl/site/search"

    staticUrl = "https://szukaj.ipn.gov.pl/site/search?q=QUERY&site=&btnG=Szukaj&client=default_frontend&output=xml_no_dtd&proxystylesheet=default_frontend&sort=date%3AD%3AL%3Ad1&wc=200&wc_mc=1&oe=UTF-8&ie=UTF-8&ud=1&exclude_apps=1&tlen=200&size=50"

    queryParams = {
        "q": "",
        "btnG": "Szukaj",
        "client": "default_frontend",
        "output": "xml_no_dtd",
        "proxystylesheet": "default_frontend",
        "sort": "date:D:L:d1",
        "wc": "200",
        "wc_mc": "1",
        "oe": "UTF-8",
        "ie": "UTF-8",
        "ud": "1",
        "exclude_apps": "1",
        "tlen": "200",
        "size": "50"
    }
    sitesEnLang = "site=&site[]=pages_enarchiwumpamieci&site[]=pages_encamps&site[]=pages_volhyniamassacre&site[]=pages_1september39&site[]=pages_centralaipn_en&site[]=pages_greaterpolanduprising"

    def __init__(self, query: str) -> None:
        self.queryParams["q"] = query

    def build(self) -> str:
        path = self.url
        query = "?" + urlencode(self.queryParams) + f"&{self.sitesEnLang}"
        url = urljoin(self.url, query)

        print(url)
        return url


def parseIPNResults(response: Response) -> list[Article]:
    soup = BeautifulSoup(response.content, "html.parser")
    all_results = soup.find_all('div', class_="res-item")

    results: list[Article] = []
    for result in all_results:
        title_link = result.find('a')
        title = title_link.get_text()
        url = title_link.get('href')
        description = ""
        for content in result.contents:
            if (content.get_text().startswith('...')):
                description = content

        results.append(Article(url, title, description))

    print('\n', results)
    return results
