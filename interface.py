from tkinter import *

BG_ROOT = "#213555"
BG_CANVAS = "#3E5879"
TEXT_COLOR = "white"
TEXT_FONT = ("Verdana", 16, "bold")

class Interface():
    def __init__(self, question_ran, answer_question_ran, function):
       self.question = question_ran
       self.answer_question = answer_question_ran
       self.answer_user = ""
       self.score = 0
       self.func = function

       self.root = Tk()
       self.root.title("Quizz Game")
       self.root.config(padx=50, pady=50, bg=BG_ROOT, highlightthickness=0)

       self.score_label = Label(bg=BG_ROOT, fg=TEXT_COLOR, text=f"Score: {self.score}", font=TEXT_FONT)
       self.score_label.grid(row=0, column=1)
       
       self.canvas = Canvas(width=600, height=400, bg=BG_CANVAS, highlightthickness=0)
       self.question_text = self.canvas.create_text(300, 200, width=280, text=self.question, font=TEXT_FONT, fill=TEXT_COLOR)
       self.canvas.grid(row= 1, column=0, columnspan=2, padx=20, pady=20) 

       b_img_true = PhotoImage(file=r"images\\true.png")
       b_img_false = PhotoImage(file=r"images\\false.png")
       
       self.button_true = Button(image=b_img_true, command=self.click_b_true)
       self.button_true.grid(row=2, column=0)
       
       self.button_false = Button(image=b_img_false, command=self.click_b_false)
       self.button_false.grid(row=2, column=1)

       self.root.mainloop()

    def new_random_question(self):
        result = self.func()
        if result is None:  
            self.canvas.itemconfig(
               self.question_text, 
               text=f"You have finished the game, and your final score is: {self.score}"
            )
            self.canvas.config(bg=BG_CANVAS)
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")   
        else:
            new_question, new_answer_question = result
            self.question = new_question
            self.answer_question = new_answer_question 
            self.canvas.itemconfig(self.question_text, text=self.question) 
            self.canvas.config(bg=BG_CANVAS)  
          
    def click_b_true(self):
       self.answer_user = "True"
       self.check_answer_user(self.answer_user)

    def click_b_false(self):
       self.answer_user = "False"
       self.check_answer_user(self.answer_user)

    def check_answer_user(self, answer_user):
      if self.answer_question == answer_user:
         self.score += 1
         self.score_label.config(text=f"Score: {self.score}") 
         self.root.after(1000, self.new_random_question)
         self.canvas.config(bg="green")
      else:
         self.root.after(1000, self.new_random_question)
         self.canvas.config(bg="red")