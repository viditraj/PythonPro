import time
from turtle import Screen
from snake import Snake
from game_info import GameInfo
from food import FoodForSnake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")
info = GameInfo()
info.display_info()

snake_food = FoodForSnake()

snake_food.food()

snake = Snake()
screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Right", fun=snake.right)
screen.onkeypress(key="Left", fun=snake.left)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    if snake.segments[0].ycor() > 299 or snake.segments[0].xcor() > 299 or snake.segments[0].ycor() < -299 \
            or snake.segments[0].xcor() < -299:
        print("Game Over")
        break
screen.exitonclick()
