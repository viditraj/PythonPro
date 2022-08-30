import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

screen = Screen()
screen.tracer(0)
l_paddle = Paddle((-387, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
screen.bgcolor("black")
score_board = ScoreBoard()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 355:
        ball.bounce_x()
        score_board.update_score(2)
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -357:
        ball.bounce_x()
        score_board.update_score(1)
    if ball.xcor() > 380:
        ball.reset_ball()
    if ball.xcor() < -380:

        ball.reset_ball()

screen.exitonclick()
