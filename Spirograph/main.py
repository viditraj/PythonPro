import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(gap_btn_circle):
    for _ in range(int(360/gap_btn_circle)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_btn_circle)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()


