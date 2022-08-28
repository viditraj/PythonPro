from turtle import Turtle


class GameInfo:
    def __init__(self):
        self.game_level = 1
        self.lives = 3

    def update_life(self):
        self.lives -= 1

    def update_level(self):
        self.game_level += 1

    def display_info(self):
        info = Turtle()
        info.color("White")
        info.hideturtle()
        info.penup()
        info.goto(x=-280, y=280)
        info.write(arg=f"Level: {self.game_level}")
        info.goto(x=-280, y=260)
        info.write(arg=f"Lives: {self.lives}")
