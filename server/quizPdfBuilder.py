from fpdf import FPDF
import pdfkit

from generator import Question


class QuizPdfBuilder():
    title: str
    sourceUrl: str
    questions: list[Question]

    def __init__(self, title: str, sourceUrl: str, questions: list[Question]):
        self.title = title
        self.sourceUrl = sourceUrl
        self.questions = questions

    def build(self):
        questionsHtml:str = ""

        for question in self.questions:
            answersHtml = ""
            for answerKey in question.answers.keys():
                answersHtml += f"<li>{answerKey}</li>"
            answersHtml = f"<ol>{answersHtml}</ol>"

            questionsHtml += f"<h3>{question.question}</h3>"
            questionsHtml += answersHtml

        html = f"""
                    <html>
                    <head>
                        <meta charset="utf-8">
                        <title>{self.title}</title>
                        <style>{""}</style>
                    </head>
                    <body class="markdown-body">
                        <h1>{self.title}</h1>
                        <a href="{self.sourceUrl}">{self.sourceUrl}</a>
                        {questionsHtml}
                    </body>
                    </html>
                    """
        return pdfkit.from_string(html, False)
