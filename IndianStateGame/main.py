from turtle import Turtle, Screen


screen = Screen()
image = "India-state.gif"
screen.addshape(image)
tit = Turtle(image)
screen.listen()
screen.exitonclick()