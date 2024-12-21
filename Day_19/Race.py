from turtle import Turtle, Screen
import random

game_start = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_choice = screen.textinput(title="All stakes in...", prompt=" Which Turtl will win the race? Enter the color : ") 
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
all_turtles = []

for i in range(len(colors)):
    racers = Turtle(shape="turtle")
    racers.color(colors[i])
    racers.penup()
    racers.goto(-230, -100 + i * 30)
    all_turtles.append(racers)

if user_choice:
    game_start = True

while game_start:
        
    for player in all_turtles:
        if player.xcor() > 230:
            game_start = False
            winner = player.pencolor()
            if winner == user_choice:
                print(f"You've won! The {user_choice} turtle is the winner!")
            else:
                print(f"Sorry, the {winner} turtle is the winner!")
        random_move = random.randint(0, 10)
        player.forward(random_move)


screen.exitonclick()