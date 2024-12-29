from data import data, questions
import random


question_number = 1
start = True

while start: 
    random_question = random.choice(questions)
    ind = questions.index(random_question)
    correct_answer = data['results'][ind]['correct_answer']
    
    print(f"{question_number}- Pregunta: {random_question}: True or False")

    usuario_answer = input("Ingresa tu respuesta: \n").capitalize()

    if usuario_answer == correct_answer:
       print("Felicitaciones, acertaste!!")
       question_number += 1
       
    else:
       print("Lo sentimos, Perdiste")
       start = False




