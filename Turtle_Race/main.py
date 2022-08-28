from turtle import Turtle, Screen
import random

colors = ["Red", "Green", "Yellow", "Blue", "Violet", "Orange"]
screen = Screen()
screen.setup(width=600, height=400)
screen.title("Turtle Race")
turtles = []
turtle_distance = [-70, -40, -10, 20, 50, 80]

user_choice = screen.textinput("Bet on turtle", "choose the color of your turtle!")
print(user_choice)


for tut in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[tut])
    new_turtle.goto(x=-280, y=turtle_distance[tut])
    turtles.append(new_turtle)
race_is_on = True

while race_is_on:
    for tut in turtles:
        if tut.xcor() > 280:
            if user_choice.lower() == tut.pencolor().lower():
                print(f"You won! {tut.pencolor()} color Turtle won the race")
            else:
                print(f"You lose! {tut.pencolor()} color Turtle won the race")
            race_is_on = False
        tut.forward(random.randint(1, 15))

screen.exitonclick()
