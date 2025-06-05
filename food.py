from turtle import Turtle
import random
from randomcolor import RandomColor

RANDOM_COLOR = RandomColor()

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(RANDOM_COLOR.generate())
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 250)
        self.goto(ran_x, ran_y)
        self.color(RANDOM_COLOR.generate())