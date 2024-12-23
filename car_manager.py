import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_POSITION_X = 325
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(STARTING_POSITION_X, random.randint(-280, 280))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self, current_level):
        add_move_speed = 0
        if current_level > 1:
            add_move_speed = MOVE_INCREMENT * current_level
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + add_move_speed)

    def reset_screen(self):
        for car in self.all_cars:
            car.clear()
            car.hideturtle()
        self.all_cars = []