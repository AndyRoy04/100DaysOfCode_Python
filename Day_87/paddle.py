from turtle import Turtle
from colors import colors
import random

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(colors))
        self.shapesize(stretch_wid=0.8, stretch_len=5)
        self.penup()
        self.goto(0, -310)
        self.steps = 30
        
    def left(self):
        new_x = self.xcor() - self.steps
        if self.xcor() > -285:
            self.setx(new_x)
            self.screen.update()
    def right(self):
        new_x = self.xcor() + self.steps
        if self.xcor() < 290:
            self.setx(new_x)
            self.screen.update()
