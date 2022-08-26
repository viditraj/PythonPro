from turtle import Turtle, colormode
import random

tim = Turtle()
colormode(255)
directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fast")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(400):
    tim.color(random_color())
    tim.forward(40)
    tim.setheading(random.choice(directions))

