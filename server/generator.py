import torch

from question_generator.questiongenerator import QuestionGenerator

generator = QuestionGenerator()

class Question:
    question: str
    answers: dict[str, bool]

    def __init__(self, question: str, answers: dict[str, bool]) -> None:
        self.question = question
        self.answers = answers


def generateQuestions(text: str) -> list[Question]:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    print(f"generating ...")

    result = generator.generate(
        article=text, answer_style="multiple_choice", num_questions=5)

    questions: list[Question] = []
    for obj in result:
        question = obj['question']
        answers: dict[str, bool] = {}

        for answer in obj['answer']:
            ans: str = answer['answer']
            isCorrect: bool = answer['correct']
            answers[ans] = isCorrect

        questionDTO = Question(question, answers)
        questions.append(questionDTO)

    print(f"finished generating.")
    return questions
    # return dummyGeneratedQuestions

dummyGeneratedQuestions: list[Question] = [
    Question('first question', {
        'first question answer 1': False,
        'first question answer 2': True,
        'first question answer 3': False
    }),
    Question('second question', {
        'second question answer 1': False,
        'second question answer 2': True,
        'second question answer 3': False
    }),
    Question('third question', {
        'third question answer 1': False,
        'third question answer 2': True,
        'third question answer 3': False
    })
]