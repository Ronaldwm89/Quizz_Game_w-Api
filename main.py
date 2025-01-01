from data import data, questions
from interface import Interface
import random
import html

def check_questions_empty():
    if len(questions) == 0:
        return True

def random_question():
    if not check_questions_empty():
            
        random_q = random.choice(questions)
        formated_question = html.unescape(random_q)

        ind = questions.index(random_q)
        correct_answer = data['results'][ind]['correct_answer']

        questions.remove(random_q)

        return formated_question, correct_answer
    else:
        return None
    
question_ran = random_question()[0]
answer_question_ran = random_question()[1]

ROOT = Interface(question_ran, answer_question_ran, random_question)