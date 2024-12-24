from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(1, 2)
        self.setheading(180)
        self.goto(300, random.randint(-250, 250))
        self.move_speed = STARTING_MOVE_DISTANCE
        self.car_list = []
        self.car_list.append(self)

    # create a new car 
    def create_car(self):
        new_car = CarManager()
        self.car_list.append(new_car)

    # making the car move
    def car_move(self):
        for car in self.car_list:
            car.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT



