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
        self.best_label= Label(text="Best: 0", fg="white", bg=THEME_COLOR)
        self.best_label.grid(column=0,row=0)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text='Some questions',
                                                     font=('Ariel', 20, 'italic'),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        ri = PhotoImage(file='images/true.png')
        wi = PhotoImage(file='images/false.png')
        self.ok_button = Button(image=ri, highlightthickness=0, borderwidth=0,command=self.good_q)
        self.ok_button.grid(column=0, row=2)
        self.wrong_button = Button(image=wi, highlightthickness=0, borderwidth=0,command=self.bad_q)
        self.wrong_button.grid(column=1, row=2)
        self.get_next_quest()
        self.window.mainloop()

    def get_next_quest(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.best_label.config(text=f"Best: {self.quiz.best}")
        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="Game Over")
            self.ok_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            with open('data.txt', 'w') as f:
                f.write(f'{self.quiz.best}')
    def good_q(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def bad_q(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_quest)

