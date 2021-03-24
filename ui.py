import tkinter

THEME_COLOR = "#375362"
FONT = "Bahnschrift"


class Ui:
    def __init__(self) -> None:
        self.answer = None

        self.window = tkinter.Tk()
        self.window.title("Quiz Game v2")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = tkinter.Canvas(
            width=500, height=500, highlightthickness=0, bg=THEME_COLOR
        )
        self.quiz_text = self.canvas.create_text(
            250, 250, text="PLACEHOLER", fill="white", font=(FONT, 24), width=400
        )
        self.points = self.canvas.create_text(
            400, 50, text="Score: 0", fill="white", font=(FONT, 12)
        )

        self.canvas.grid(column=1, row=1, columnspan=3)

        self.answer_true = tkinter.Button()
        self.check_image = tkinter.PhotoImage(file="images/true.png")
        self.answer_true.config(image=self.check_image, width=100, height=100)
        self.answer_true.grid(column=3, row=2)

        self.answer_false = tkinter.Button()
        self.x_image = tkinter.PhotoImage(file="images/false.png")
        self.answer_false.config(image=self.x_image, width=100, height=100)
        self.answer_false.grid(column=1, row=2)

    def change_text(self, question, score):
        self.canvas.itemconfig(self.quiz_text, text=question)
        self.canvas.itemconfig(self.points, text=score)

