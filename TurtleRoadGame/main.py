import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
Score = Scoreboard()
player = Player()
Car = CarManager()
screen.listen()
screen.onkeypress(key="w", fun=player.move_up)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if Score.level < 12:
        Car.generate_car(Score.level)
    Car.move_car()
    if Score.level > 12:
        game_is_on = False
    if player.ycor() > 290:
        Score.increase_level()
        Car.level_up()
        player.reset_position()
    for car in Car.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
Score.game_over()
screen.exitonclick()


