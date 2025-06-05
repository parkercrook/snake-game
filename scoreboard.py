import time
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(x=0, y=250)
        self.current_score = 0
        self.high_score = 0
        self.print_score()

    def print_score(self):
        self.write(arg=f"Score: {self.current_score} - High Score: {self.high_score}", align="center", font=("Lora", 20, "normal"))

    def update_score(self):
        self.clear()
        self.print_score()

    def increase_score(self):
        self.current_score += 1

    def reset_scoreboard(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.update_score()