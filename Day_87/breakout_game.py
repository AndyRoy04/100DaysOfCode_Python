import time
from turtle import *
from paddle import Paddle
from ball import Ball
from brick_wall import BrickWall
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(700, 700)
screen.bgcolor('black')
screen.title('Breakout Game')
screen.colormode(255)   # accept color numbers up to 255
screen.tracer(0)  # nothing is drawn unto the screen untill this is been updated

def game_over():    # Stopping the game
    global game_on
    game_on = False
    
game_paddle = Paddle()
game_ball = Ball()
brick_wall = BrickWall()
scoreboard = ScoreBoard()

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
    elif game_ball.ycor() > 330:    # Ceiling Bounce
        game_ball.bounce_y()
    elif game_ball.ycor() <= -295 and abs(game_ball.xcor() - game_paddle.xcor()) < 65 and game_ball.y_move < 0:
        game_ball.sety(-295)    # Instantly snap the ball slightly above
        game_ball.bounce_y()
        
        if game_ball.xcor() < game_paddle.xcor():          
            game_ball.force_left() # Ball hit the left side it move left
        else:            
            game_ball.force_right() # Ball hit the right side it move right
            
    elif game_ball.ycor() <= -355:      # Out of bound game over
        lives_left = scoreboard.lose_life()
        if lives_left <= 0:
            scoreboard.game_over()
            game_on = False
        else:
            game_ball.reset()
            time.sleep(1)

        
    # Detecting the brick collision and performing action
    
    closest_brick = None
    closest_distance = float('inf')     # starts at infinity
    
    for brick in brick_wall.brick_list.copy():  # create a shallow copy of the list to edit or wall.bricks[:]
        if brick.isvisible():
            dist = game_ball.distance(brick)            
            if dist < 28 and dist < closest_distance:
                closest_distance = dist
                closest_brick = brick
                
    if closest_brick is not None:
        horizontal_diff = abs(game_ball.xcor() - closest_brick.xcor())
        vertical_diff = abs(game_ball.ycor() - closest_brick.ycor())    

        if horizontal_diff > vertical_diff:
            game_ball.bounce_x()
        else:
            game_ball.bounce_y()
        brick_wall.destroy(closest_brick)            
        scoreboard.increment()
        game_ball.speed_up()
                    
    if len(brick_wall.brick_list) == 0:     # User Won
        scoreboard.you_win()
        game_on = False
            
screen.exitonclick()