import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.best = 0
        try:
            with open('data.txt') as f:
                self.best = int(f.read())
        except (FileNotFoundError, ValueError):
            with open('data.txt', mode='w') as f:
                f.write('0')
        else:
            with open('data.txt') as f:
                self.best = int(f.read())
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            if self.best <= self.score:
                self.best = self.score
            return True
        else:
            return False
