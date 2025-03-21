# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create_car()
    car_manager.move_cars()

    # when turtle crosses finish line:
    # reset turtle, increase level and car speed
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.level_up()

    # check if the car has crashed into any of the cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
