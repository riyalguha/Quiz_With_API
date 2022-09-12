from question_model import Question
#from data import question_data
from quiz_brain import QuizBrain
import requests

question_bank = []
response=requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
question_data=response.json()['results']
# print(question_bank)
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
#
#
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
