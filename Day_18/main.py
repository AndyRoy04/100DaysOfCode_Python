# from turtle import Turtle, Screen

# jack = Turtle()
# jack.shape("turtle")
# jack.color('grey')

# def move_turtle():
#     jack.forward(200)
#     jack.right(90)
    
# for i in range(4):
#     move_turtle()

# my_screen = Screen()
# my_screen.exitonclick()


## Importing modules
# import heroes
# print(heroes.gen())  # prints "I am Iron Man"  # prints "I


# # Drawing dashed lines in Python
# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()
# tim.shape("turtle")

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# screen.exitonclick()


# ## Drawing different shapes
# from turtle import Turtle, Screen
# import random

# tim = Turtle()
# screen = Screen()
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tim.speed(10)

# number_of_sides = 3
# while number_of_sides != 11:
#     angle = 360 / number_of_sides
#     tim.color(random.choice(colors))

#     for _ in range(number_of_sides):
#         tim.forward(100)
#         tim.right(angle)

#     number_of_sides += 1

# screen.exitonclick()


## Creating a random walk program
# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)
# # screen = Screen()

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
# # colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# direction = [0, 90, 180, 270]
# tim.width(15)
# tim.speed('fastest')

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(25)
#     tim.setheading(random.choice(direction))

# # screen.exitonclick()


# ## Creating a spirograph
# import turtle as t
# import random
# tim = t.Turtle()
# t.colormode(255)
# tim.speed('fastest')

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# def size_of_gap(gap):
#     for i in range(int(360/gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + gap)

# size_of_gap(5)

# screen = t.Screen()
# screen.exitonclick()


