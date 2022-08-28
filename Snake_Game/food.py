import random
from turtle import Turtle


class FoodForSnake:

    def __init__(self):
        pass

    def food(self):
        food = Turtle()
        food.pensize(10)
        food.color("#FF6363")
        food.hideturtle()
        food.penup()
        xcod = random.randint(-299, 299)
        ycod = random.randint(-299, 250)
        food.goto(x=xcod, y=ycod)
        food.pendown()
        food.forward(1)
