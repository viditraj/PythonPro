from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.speed = 0.01

    def create_snake(self):
        for i in range(0, 3):
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(-i * 20, 0)
            self.segments.append(segment)
            self.segments[0].color("violet")

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg_num - 1].xcor()
            y_pos = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_pos, y_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)

    def add_segment(self):
        i = len(self.segments)-1
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(-i * 20, 0)
        self.segments.append(segment)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
