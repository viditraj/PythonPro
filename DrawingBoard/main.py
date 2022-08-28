from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.setheading(0)
    tim.forward(10)


def move_backward():
    tim.setheading(180)
    tim.forward(10)


def move_up():
    tim.setheading(90)
    tim.forward(10)


def move_down():
    tim.setheading(270)
    tim.forward(10)


screen.listen()
screen.onkeypress(key="d", fun=move_forward)
screen.onkeypress(key="a", fun=move_backward)
screen.onkeypress(key="w", fun=move_up)
screen.onkeypress(key="s", fun=move_down)
screen.onkeypress(key="q", fun=tim.penup)
screen.onkeypress(key="e", fun=tim.pendown)
screen.onkeypress(key="x", fun=screen.reset)
screen.exitonclick()
