from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.final_score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {self.final_score}", bg=THEME_COLOR, font=("Arial", 10, "normal"), fg="White")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150,
                                                125,
                                                width=280,
                                                text="Some Question Text",
                                                font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        correct_img = PhotoImage(file="./images/true.png")
        wrong_img = PhotoImage(file="./images/false.png")

        self.correct_button = Button(image=correct_img, relief=FLAT, highlightthickness=0, borderwidth=0,
                                     command=self.true_passed)
        self.correct_button.grid(column=1, row=2)

        self.wrong_button = Button(image=wrong_img, relief=FLAT, highlightthickness=0, borderwidth=0, command=self.false_passed)
        self.wrong_button.grid(column=0, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.reset_canvas()
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the Quiz!")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_passed(self):
        if self.quiz.check_answer("True"):
            self.final_score += 1
            self.score.config(text=f"Score: {self.final_score}")
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def false_passed(self):
        if self.quiz.check_answer("False"):
            self.final_score += 1
            self.score.config(text=f"Score: {self.final_score}")
            self.give_feedback(True)
        else:
            self.give_feedback(False)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#59CE8F")
        else:
            self.canvas.config(bg="#FF5D5D")
        self.canvas.itemconfig(self.question, fill="white")
        self.window.after(500, self.get_next_question)

    def reset_canvas(self):
        self.canvas.config(bg="White")
        self.canvas.itemconfig(self.question, fill=THEME_COLOR)
