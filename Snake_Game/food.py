import random
from turtle import Turtle


class FoodForSnake:

    def __init__(self):
        self.food = Turtle()
        self.food.shape("circle")
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.color("#FF6363")
        self.food.speed("fastest")
        self.food.penup()
        self.refresh()

    def refresh(self):
        xcode = random.randint(-290, 290)
        ycode = random.randint(-290, 250)
        self.food.goto(x=xcode, y=ycode)

