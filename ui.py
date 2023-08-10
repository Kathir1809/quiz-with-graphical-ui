THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.quiz_score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.text = Label(text=f"Score:{self.quiz_score}", bg=THEME_COLOR, foreground="white", font=("Arial Black", 12, "bold"))
        self.text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.tt1 = self.canvas.create_text(150, 125,
                                           width=280,
                                           text="Your question places here",
                                           font=("Arial", 12, "bold"))

        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=40)

        self.img1 = PhotoImage(file="./images/true.png")
        self.img2 = PhotoImage(file="./images/false.png")

        self.true = Button(image=self.img1, highlightthickness=0, command=lambda: self.true_button("true"))
        self.true.grid(row=2, column=0)
        self.false = Button(image=self.img2, highlightthickness=0, command=lambda: self.false_button("false"))
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.tt1, text=self.question)
            self.text.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.tt1, text="You've reached to end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_button(self, user):
        self.next = self.quiz.check_answer(user)
        self.feedback(self.next)

    def false_button(self, user):
        self.next_q = self.quiz.check_answer(user)
        self.feedback(self.next_q)

    def feedback(self, a):
        if a:
            self.canvas.config(bg="green")
            self.quiz_score += 1
        else:
            self.canvas.config(bg="red")

        self.timer = self.window.after(1000, self.get_next_question)