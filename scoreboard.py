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
        self.print_score()

    def print_score(self):
        self.write(arg=f"Score: {self.current_score}", align="center", font=("Lora", 20, "normal"))

    def update_score(self):
        self.current_score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER", align="center", font=("Lora", 20, "normal"))