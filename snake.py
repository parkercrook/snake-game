from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_pos = 0
        for _ in range(1, 4):
            self.add_segment(x_pos)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def go_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def go_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def go_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def go_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def add_segment(self, x_pos):
        segment = Turtle()
        segment.setx(x_pos)
        segment.penup()
        segment.shape("square")
        segment.color("white")
        x_pos -= 20
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].xcor())

    def reset_snake(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]