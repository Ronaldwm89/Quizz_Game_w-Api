from tkinter import *

BG_ROOT = "#213555"
BG_CANVAS = "#3E5879"
TEXT_COLOR = "white"
TEXT_FONT = ("Verdana", 16, "bold")

class Interface:
     def __init__(self, question, answer_q, function):
          self.questions = question
          self.answer_question = answer_q
          self.func = function
          self.answer_user = ""
          self.score = 0


          self.root = Tk()
          self.root.title("Quizz Game")
          self.root.config(padx=50, pady=50, bg=BG_ROOT, highlightthickness=0)
          
          self.score_label = Label(bg=BG_ROOT, fg=TEXT_COLOR, text=f"Score: {self.score}", font=TEXT_FONT)
          self.score_label.grid(row=0, column=1) 

          self.canvas = Canvas()
          self.canvas.config(width=600, height=400, bg=BG_CANVAS, highlightthickness=0)
          self.question_text = self.canvas.create_text(300,200, width=280, text=f"Primera Pregunta", font=TEXT_FONT, fill=TEXT_COLOR)
          self.canvas.grid(padx=20, pady=20, row=1, column=0, columnspan=2)

          img_btrue = PhotoImage(file=r"images\\true.png")
          img_bfalse = PhotoImage(file=r"images\\false.png")

          self.button_true = Button(image=img_btrue, command=self.click_true)
          self.button_true.grid(row=2, column=0)

          self.button_false = Button(image=img_bfalse, command=self.click_false)
          self.button_false.grid(row=2, column=1)


          self.random_question()
          self.root.mainloop()

   
     def random_question(self):
          new_question, new_answer_q = self.func()
          self.questions = new_question
          self.answer_question = new_answer_q
          self.canvas.itemconfig(self.question_text, text=f"{new_question}")
          self.canvas.config(bg=BG_CANVAS)

          
     def click_true(self):
          self.answer_user = "True"
          self.feedback_display()

     def click_false(self):
          self.answer_user = "False"
          self.feedback_display()

     def check_answer(self, answer_user):
          if self.answer_question == answer_user:
               return True
          else:
               return False
               
     def feedback_display(self):
          guess_true = self.check_answer(self.answer_user)
          if guess_true:
               self.root.after(1000, self.random_question)
               self.score += 1
               self.score_label.config(text=f"Score: {self.score}")
               self.canvas.config(bg="green")
          else:
               self.root.after(1000, self.random_question)
               self.canvas.config(bg="red")
