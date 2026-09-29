from turtle import Turtle
from colors import colors
import random

BRICK_ROWS = random.choice(range(6, 9))
BRICK_COLS = 10
BRICK_WIDTH = 60
BRICK_HEIGHT = 10
BRICK_GAP = 9
START_Y = 260

class BrickWall(Turtle):
    
    def __init__(self):
        super().__init__()
        self.brick_list = []
        self.draw_wall()
        
    def draw_wall(self):
        for row in range(BRICK_ROWS):
            color = random.choice(colors)
            for col in range(BRICK_COLS):
                brick = Turtle()
                brick.shape('square')
                brick.penup()
                brick.shapesize(stretch_wid=0.3, stretch_len=3)
                brick.color(color)
                x_pnt = -315 + col * (BRICK_WIDTH + BRICK_GAP)
                y_pnt = START_Y - row * (BRICK_HEIGHT + BRICK_GAP)
                brick.goto(x_pnt, y_pnt)
                self.brick_list.append(brick)
                
    def destroy(self, brick):
        brick.hideturtle()
        if brick in self.brick_list:
            self.brick_list.remove(brick)