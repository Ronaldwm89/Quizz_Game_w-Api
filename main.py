from data import data, questions
from interface import Interface
import random
import html

def random_question():
   ran_question = random.choice(questions)
   formated_question = html.unescape(ran_question)
   ind = questions.index(ran_question)
   correct_answer = data['results'][ind]['correct_answer']
   
   return formated_question, correct_answer

   
question, answer_q = random_question()
UI = Interface(question, answer_q, random_question)
