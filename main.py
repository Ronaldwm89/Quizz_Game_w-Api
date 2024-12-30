from data import data, questions
from interface import Interface
import random
import html



score_number = 1

def random_question():
   ran_question = random.choice(questions)
   formated_question = html.unescape(ran_question)
   ind = questions.index(ran_question)
   correct_answer = data['results'][ind]['correct_answer']

    
   return score_number, formated_question, correct_answer


question = random_question()
UI = Interface(question)
#usuario_answer = input("Ingresa tu respuesta: \n").capitalize()

'''
if usuario_answer == correct_answer:
   score_number += 1
   print(f"Felicitaciones, acertaste!! Score = {score_number-1}")    
else:
   print(f"Lo sentimos, Perdiste, puntuacion final: {score_number-1}")
   '''




