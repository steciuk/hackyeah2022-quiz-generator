from typing import Union
from urllib.parse import urlencode, urljoin

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from pydantic.main import BaseModel
from requests import Response

app = FastAPI()


class GeneratorRequest(BaseModel):
    sourceUrl: str


@app.post("/generate")
def read_root(req: GeneratorRequest):
    if req.sourceUrl.endswith(".pdf"):
        print("implement PDF")
    else:
        return queryIPNSourceFromWebsite(req.sourceUrl)


@app.get("/{query}")
def queryIPN(query: str, q: Union[str, None] = None) -> None:
    request_url: str = RequestBuilder(query).build()
    response = requests.get(request_url)
    query_results = parseIPNResults(response)
    return query_results


def queryIPNSourceFromWebsite(url: str) -> list[str]:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    all_paragraphs = soup.find_all('p')
    all_paragraphs_texts: list[str] = []
    for p in all_paragraphs:
        all_paragraphs_texts.append(p.getText())

    return all_paragraphs_texts


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


class Result:
    url: str
    title: str
    description: str

    def __init__(self, url: str, title: str, description: str):
        self.url = url
        self.title = title
        self.description = description


def parseIPNResults(response: Response) -> list[Result]:
    soup = BeautifulSoup(response.content, "html.parser")
    all_results = soup.find_all('div', class_="res-item")

    results: list[Result] = []
    for result in all_results:
        title_link = result.find('a')
        title = title_link.get_text()
        url = title_link.get('href')
        description = ""
        for content in result.contents:
            if (content.get_text().startswith('...')):
                description = content

        results.append(Result(url, title, description))

    print('\n', results)
    return results
