from fpdf import FPDF

from generator import Question


class QuizPdfBuilder(FPDF):
    def addTitle(self, title):
        title = title.encode('latin-1', 'replace').decode('latin-1')
        # Arial bold 15
        self.set_font('Arial', 'B', 15)

        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)

        # # Colors of frame, background and text
        # self.set_draw_color(0, 80, 180)
        # self.set_fill_color(230, 230, 0)
        # self.set_text_color(220, 50, 50)
        # # Thickness of frame (1 mm)
        # self.set_line_width(1)

        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

    def addQuestionTitle(self, title):
        title = title.encode('latin-1', 'replace').decode('latin-1')

        # Arial 12
        self.set_font('Arial', '', 12)

        # Background color
        # self.set_fill_color(200, 220, 255)

        # Title
        self.cell(0, 6, title, 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def addQuestionAnswers(self, question: Question):
        # # Read text file
        # with open(name, 'rb') as fh:
        #     txt = fh.read().decode('latin-1')

        # Times 12
        self.set_font('Times', '', 12)

        for index, (answer, isCorrect) in enumerate(question.answers.items()):
            answer = answer.encode('latin-1', 'replace').decode('latin-1')

            formattedAnswer = f"{index + 1}) {answer}"
            # Output justified text
            self.multi_cell(0, 5, formattedAnswer)
            # Line break
            self.ln()

        # Mention in italics
        # self.set_font('', 'I')
        # self.cell(0, 5, '(end of excerpt)')