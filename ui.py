from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("QuizAPI")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250,bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Some questions', font=('Ariel', 20, 'italic'),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)
        ri=PhotoImage(file='images/true.png')
        wi=PhotoImage(file='images/false.png')
        self.ok_button=Button(image=ri,highlightthickness=0,borderwidth=0)
        self.ok_button.grid(column=0,row=2)
        self.wrong_button=Button(image=wi,highlightthickness=0,borderwidth=0)
        self.wrong_button.grid(column=1,row=2)
        self.window.mainloop()
