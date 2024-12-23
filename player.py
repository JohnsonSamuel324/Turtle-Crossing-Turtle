from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("darkseagreen")
        self.level_setup()

    def level_setup(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def finished_level(self):
        self.level_setup()