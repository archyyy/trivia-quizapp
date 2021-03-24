import data
import html


class Brain:
    def __init__(self) -> None:
        self.quiz = data.Question()
        self.questions_list = []
        self.answers_list = []
        self.i = 0
        self.score = 0

    def generate(self) -> None:
        for self.i in range(len(self.quiz.results)):
            self.result = self.quiz.results[self.i]
            self.questions_list.append(
                html.unescape(self.result["question"])
            )
            self.answers_list.append(self.result["correct_answer"])
            self.i += 1

    def next_question(self, index):
        self.current_question = self.questions_list[index]
        self.current_answer = self.answers_list[index]

    def check_and_score(self, user):
        if self.current_answer == user:
            self.score += 1
            return True
        return False
