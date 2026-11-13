# For unescape
import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
    
    # Is any question left?
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # To get next question
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        # print(vars(self.current_question))
        self.question_number += 1
        c_ques = html.unescape(self.current_question.question)
        return f"Q{self.question_number}: {c_ques}"
        # user_answer = input(f"Q{self.question_number}: {c_ques} (True/False): ")
        # self.check_answer(user_answer)

    # Check correct answer
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            # print(f"You got it right!")
            return True
        else:
            # print(f"You are wrong!")
            return False

        # print(f"The correct answer is: {correct_answer}")
        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")