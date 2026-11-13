from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    ques    = question["question"]
    ans     = question["correct_answer"]

    new_question = QuestionModel(q_question=ques, q_answer=ans)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions:
#     quiz.next_question()

# print(f"You have completed the quiz!")
# print(f"Your final score was: {quiz.score} / {quiz.question_number}")