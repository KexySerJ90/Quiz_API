from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizAPI")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text='Some questions',
                                                     font=('Ariel', 20, 'italic'),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        ri = PhotoImage(file='images/true.png')
        wi = PhotoImage(file='images/false.png')
        self.ok_button = Button(image=ri, highlightthickness=0, borderwidth=0)
        self.ok_button.grid(column=0, row=2)
        self.wrong_button = Button(image=wi, highlightthickness=0, borderwidth=0)
        self.wrong_button.grid(column=1, row=2)
        self.get_next_quest()
        self.window.mainloop()

    def get_next_quest(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def good_q(self):
        self.quiz.check_answer("True")

    def bad_q(selfs):
        self.quiz.check_answer("False")