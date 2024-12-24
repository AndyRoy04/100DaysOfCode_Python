from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, 'Up')

car_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car_move()
    
    car_counter += 1
    if car_counter == 6:
        car_manager.create_car()
        car_counter = 0

    if player.finish_line():
        player.go_to_start()
        scoreboard.update()
        car_manager.increase_speed()

    # detect collision with car
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()



