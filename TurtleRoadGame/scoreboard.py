from turtle import Turtle

FONT = ("Courier", 13, "bold")
FONT_GAME_OVER = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.write_score()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write_score()

    def write_score(self):
        self.goto(-280, 260)
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(-100, 0)
        self.write(arg="Game Over!!!", font=FONT_GAME_OVER)


