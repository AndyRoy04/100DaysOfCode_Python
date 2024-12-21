from turtle import Turtle, Screen

ball = Turtle()
screen = Screen()

def move_left():
    ball.left(10)
def move_right():
    ball.right(10)
def move_forward():
    ball.forward(10)
def move_backward():
    ball.backward(10)
def clear():
    ball.clear()
    ball.penup()
    ball.home()
    ball.pendown()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()



# from turtle import Turtle, Screen
# import random

# game_start = False
# screen = Screen()
# screen.setup(width = 500, height = 400)
# user_choice = screen.textinput(title="All stakes in...", prompt=" Which Turtl will win the race? Enter the color : ") 
# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# all_turtles = []
# y_cordinate = -100

# for number in range(len(colors)):
#     new_turtle = Turtle(shape='turtle')
#     new_turtle.penup()
#     new_turtle.color(colors[number])
#     new_turtle.goto(x=-230, y=y_cordinate)
#     y_cordinate += 30
#     all_turtles.append(new_turtle)

# if user_choice:
#     game_start = True

# while game_start:

#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             game_start = False
#             turtle_color = turtle.pencolor()
#             if turtle_color == user_choice:
#                 print(f"You have won the race with {turtle_color} turtle")
#             else:
#                 print(f"Sorry, you have lost the race. The winner is {turtle_color} turtle")
            
#         random_step = random.randint(0, 10)
#         turtle.forward(random_step)

# screen.exitonclick()