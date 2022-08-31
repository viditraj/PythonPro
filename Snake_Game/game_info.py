from turtle import Turtle


class GameInfo:
    def __init__(self):
        self.score = 0
        self.info = Turtle()
        with open("data.txt") as data:
            self.high_score = int(data.read())

    def update_score(self):
        self.score += 1
        self.reset_info()

    def display_info(self):
        self.info.clear()
        self.info.color("White")
        self.info.hideturtle()
        self.info.penup()
        self.info.goto(x=-130, y=270)
        self.info.write(arg=f"Score:{self.score}  High Score:{self.high_score}", font=("Courier", 15, "normal"))

    def reset_info(self):
        self.display_info()

    def reset_game(self):

        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.display_info()

    # def end_game(self):
    #     self.info.color("White")
    #     self.info.hideturtle()
    #     self.info.penup()
    #     self.info.goto(x=-80, y=0)
    #     self.info.write(arg="Game Over !!!", font=("Courier", 20, "normal"))
