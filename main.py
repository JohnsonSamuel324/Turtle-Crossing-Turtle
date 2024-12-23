import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "Up")
screen.onkeypress(player.move_forward, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars(scoreboard.current_level)

    # If player reaches goal
    if player.ycor() >= 280:
        car_manager.reset_screen()
        player.finished_level()
        scoreboard.finished_level()

    # If car hits player
    for car in car_manager.all_cars:
        if player.distance(car) <= 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()