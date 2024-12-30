from tkinter import *


BG_ROOT = "#213555"
BG_CANVAS = "#3E5879"
TEXT_COLOR = "white"
TEXT_FONT = ("Verdana", 16, "bold")

class Interface:

    def __init__(self, question):
         self.questions = question[1]

         self.root = Tk()
         self.root.title("Quizz Game")
         self.root.config(padx=50, pady=50, bg=BG_ROOT)
       
         self.score = Label(fg=TEXT_COLOR, text=f"Score: 0", font=TEXT_FONT, bg=BG_ROOT)
         self.score.grid(row=0,column=1)

        

         self.canvas = Canvas(height=400, width=600, bg=BG_CANVAS, highlightthickness=0)
         self.questions_text = self.canvas.create_text(300, 200, font=TEXT_FONT, fill=TEXT_COLOR, text="1era Pregunta")
         self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

         img_true = PhotoImage(file=r"images\true.png")
         img_false = PhotoImage(file=r"images\false.png")

         self.button_true = Button()
         self.button_true.config(image=img_true)
         self.button_true.grid(row=2, column=0)

         self.button_false = Button()
         self.button_false.config(image=img_false)
         self.button_false.grid(row=2, column=1)

         self.next_question()
         self.root.mainloop()


    def next_question(self):
         q_text = self.questions
         self.canvas.itemconfig(self.questions_text, text=f"{q_text}")
         



