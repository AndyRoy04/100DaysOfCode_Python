from turtle import *
from paddle import Paddle


screen = Screen()
screen.setup(700, 700)
screen.bgcolor('black')
screen.title('Breakout Game')
screen.tracer(0)  # nothing is drawn unto the screen untill this is been updated

game_paddle = Paddle((0, -325))
screen.update()

screen.exitonclick()