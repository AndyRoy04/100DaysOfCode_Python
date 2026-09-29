from turtle import Turtle
from colors import colors
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.color(random.choice(colors))
        self.penup()
        self.goto(0, -295)
        self.x_move = 7
        self.y_move = 7
        self.move_speed = 0.07
        
    def move(self):
        self.new_x = self.xcor() + self.x_move
        self.new_y = self.ycor() + self.y_move
        self.goto(self.new_x, self.new_y)
        
    def bounce_x(self):
        self.x_move *= -1
        if self.move_speed > 0.03:
            self.move_speed *= 0.95
        
    def bounce_y(self):
        self.y_move *= -1
        
    def force_left(self):       # Make x_move always negative  
        self.x_move = -abs(self.x_move)
            
    def force_right(self):      # Make x_move always positive
        self.x_move = abs(self.x_move)

    def speed_up(self):
        if self.move_speed > 0.025:
            self.move_speed *= 0.97
        
    def reset(self):
        self.goto(0, 0)
        self.y_move     = 7
        self.x_move     = random.choice([-7, 7])
        self.move_speed = 0.04
