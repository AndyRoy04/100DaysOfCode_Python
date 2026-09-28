from turtle import Turtle
from colors import colors
import random

BRICK_ROWS = random.choice(range(6, 9))
BRICK_COLS = 10
BRICK_WIDTH = 60
BRICK_HEIGHT = 10
BRICK_GAP = 10
START_Y = 250

class BrickWall(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.brick_list = []
        self.draw_wall()
        
    def draw_wall(self):
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                color = random.choice(colors)
                brick = Turtle()
                brick.shape('square')
                brick.penup()
                brick.shapesize(stretch_wid=0.25, stretch_len=3)
                brick.color(color)
                x_pnt = -318 + col * (BRICK_WIDTH + BRICK_GAP)
                y_pnt = START_Y - row * (BRICK_HEIGHT + BRICK_GAP)
                brick.goto(x_pnt, y_pnt)
                self.brick_list.append(brick)
                
    def destroy(self, brick):
        self.hideturtle()
        self.brick_list.remove(brick)