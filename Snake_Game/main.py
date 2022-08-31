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

snake = Snake()
screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Right", fun=snake.right)
screen.onkeypress(key="Left", fun=snake.left)
game_is_on = True
snake_speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(snake_speed)
    snake.move()
    if snake.segments[0].ycor() > 299 or snake.segments[0].xcor() > 299 or snake.segments[0].ycor() < -299 \
            or snake.segments[0].xcor() < -299:
        time.sleep(1)
        info.reset_game()
        snake.reset_snake()
    elif snake.segments[0].distance(snake_food.food) < 15:
        snake_food.refresh()
        snake.add_segment()
        info.update_score()
        info.display_info()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            time.sleep(1)
            info.reset_game()
            snake.reset_snake()


screen.exitonclick()
