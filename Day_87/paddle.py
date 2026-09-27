from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=6)
        self.penup()
        self.goto(position)