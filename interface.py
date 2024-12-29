from tkinter import *

BG_ROOT = "#213555"
BG_CANVAS = "#3E5879"
TEXT_COLOR = "#D8C4B6"
TEXT_FONT = ("Verdana", 16, "bold")


root = Tk()
root.title("Quizz Game")
root.config(padx=50, pady=50, bg=BG_ROOT)

score = Label(fg=TEXT_COLOR, text="Score: 1", font=TEXT_FONT, bg=BG_ROOT)
score.grid(row=0,column=1)


img_true = PhotoImage(file=r"images\true.png")
img_false = PhotoImage(file=r"images\false.png")

canvas = Canvas(height=400, width=600, bg=BG_CANVAS, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

button_true = Button()
button_true.config(image=img_true)
button_true.grid(row=2, column=0)

button_false = Button()
button_false.config(image=img_false)
button_false.grid(row=2, column=1)



root.mainloop()

