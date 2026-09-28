from turtle import *
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(700, 700)
screen.bgcolor('black')
screen.title('Breakout Game')
screen.tracer(0)  # nothing is drawn unto the screen untill this is been updated

def game_over():    # Stopping the game
    global game_on
    game_on = False
    
game_paddle = Paddle((0, -325))
game_ball = Ball()
screen.update()

screen.listen()
screen.onkeypress(game_paddle.left, 'Left')
screen.onkeypress(game_paddle.right, 'Right')
screen.onkey(game_over, 'Return')

game_on = True
while game_on:
    time.sleep(game_ball.move_speed)
    screen.update()
    game_ball.move()
    
    # Left and Right Wall Bounces
    if game_ball.xcor() >= 330 or game_ball.xcor() <= -335:
        game_ball.bounce_x()
    elif game_ball.ycor() > 335:    # Ceiling Bounce
        game_ball.bounce_y()
    elif game_ball.ycor() <= -310 and abs(game_ball.xcor() - game_paddle.xcor()) < 65:
        game_ball.sety(-310)    # Instantly snap the ball slightly above
        game_ball.bounce_y()
        
        if game_ball.xcor() < game_paddle.xcor():          
            game_ball.force_left() # Ball hit the left side it move left
        else:            
            game_ball.force_right() # Ball hit the right side it move right
            
    elif game_ball.ycor() <= -400:  # Out of Bounds
        game_ball.reset()
    

screen.exitonclick()