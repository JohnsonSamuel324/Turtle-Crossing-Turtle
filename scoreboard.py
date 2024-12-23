from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard:
    def __init__(self):
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(-200, 250)
        self.current_level = 1
        self.scoreboard.write(f"Level : {self.current_level}", False, "center", FONT)

    def finished_level(self):
        self.current_level += 1
        self.scoreboard.clear()
        self.scoreboard.write(f"Level : {self.current_level}", False, "center", FONT)

    def game_over(self):
        self.scoreboard.goto(0,0)
        self.scoreboard.write("GAME OVER", False, "center", FONT)
