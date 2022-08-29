from turtle import Turtle


class GameInfo:
    def __init__(self):
        self.game_level = 1
        self.lives = 3
        self.score = 0
        self.info = Turtle()

    def update_life(self):
        self.lives -= 1

    def update_level(self):
        self.game_level += 1

    def update_score(self):
        self.score += 1
        self.reset_info()

    def display_info(self):
        self.info.color("White")
        self.info.hideturtle()
        self.info.penup()
        self.info.goto(x=-40, y=270)
        self.info.write(arg=f"Score: {self.score}", font=("Courier", 15, "normal"))

    def reset_info(self):
        self.info.reset()
        self.display_info()

    def end_game(self):
        self.info.color("White")
        self.info.hideturtle()
        self.info.penup()
        self.info.goto(x=-80, y=0)
        self.info.write(arg="Game Over !!!", font=("Courier", 20, "normal"))
