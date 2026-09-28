from turtle import Turtle
from colors import colors
import random

class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.location = location
        self.shape("square")
        self.color(random.choice(colors))
        self.shapesize(stretch_wid=0.5, stretch_len=6)
        self.penup()
        self.goto(location)
        
    def left(self):
        if self.xcor() > -285:
            new_x = self.xcor() - 25
            self.goto(new_x, self.ycor())
            self.screen.update()
    def right(self):
        if self.xcor() < 290:
            new_x = self.xcor() + 25
            self.goto(new_x, self.ycor())
            self.screen.update()
