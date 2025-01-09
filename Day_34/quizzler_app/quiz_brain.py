import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text) # the html.unescape() method helpd deal with HTML entities
        return f"Q.{self.question_number}: {question_text}"

    def check_answer(self, user_Choice):
        correct_answer = self.current_question.answer
        if user_Choice.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

