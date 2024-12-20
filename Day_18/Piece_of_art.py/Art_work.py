# Creating dotted points of art
import turtle as t
import random
from colors import colors

def move_turtle():
    ball.hideturtle()
    ball.penup()
    ball.goto(-200, -200)

t.colormode(255)
ball = t.Turtle()
move_turtle()
ball.speed('fast')

y_intercept = -200
for i in range(10):    
    for j in range(10):
        ball.dot(30, random.choice(colors))
        ball.pu()
        ball.forward(50)
    y_intercept += 50
    ball.goto(-200, y_intercept)
ball.hideturtle()
screen = t.Screen()
screen.exitonclick()