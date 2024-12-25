# from turtle import Turtle, Screen

# snake = Turtle('square')
# snake.penup()
# screen = Screen()
# screen.setup(width=700, height=450)

# def move_left():
#     snake.setheading(180)
# def move_right():
#     snake.setheading(0)
# def up():
#     snake.setheading(90)
# def down():
#     snake.setheading(270)

# def clear():
#     snake.clear()
#     snake.penup()
#     snake.home()

# screen.listen()
# screen.onkey(up, 'Up')
# screen.onkey(down, 'Down')
# screen.onkey(move_left, 'Left')
# screen.onkey(move_right, 'Right')
# screen.onkey(clear, 'c')

# game_on = True
# while game_on:
#     snake.forward(5)
#     if snake.xcor() >= 350 or snake.ycor() >= 225:
#         snake.home()
#     elif snake.xcor() <= -350 or snake.ycor() <= -225:
#         snake.home()

    


# screen.exitonclick()



# class Animal():
#     def __init__(self):
#         self.eyes = 2

#     def breathe(self):
#         print("Inhale, exhale")

# class Bird(Animal):
#     def __init__(self):
#         super().__init__()
#         self.wings = 2

#     def breathe(self):
#         '''Bird breathing'''
#         super().breathe()
#         print("Shake, shake")
#     def fly(self):
#         print("Flap, flap")

# sample = Bird()
# sample.breathe()
# sample.fly()
# print(sample.eyes)


# import turtle

# t = turtle.Turtle()

# # Write text with different options
# t.hideturtle()
# t.penup()
# t.write("Python is fun!", move=False, align="right", font=("Courier", 24, "bold"))
# t.write("Python is fun!", move=True, align="left", font=("Courier", 24, "bold"))

# turtle.done()

# from turtle import Turtle, Screen
# import time

# screen = Screen()
# screen.setup(600, 600)
# screen.tracer(0)
# segments = []

# for i in range(3):
#     snake = Turtle('square')
#     snake.pu()
#     snake.goto(i*-20, 0)
#     segments.append(snake)

# def move_left():
#     if segments[0].heading() != 0:
#         segments[0].setheading(180)
# def move_right():
#     if segments[0].heading() != 180:
#         segments[0].setheading(0)
# def up():
#     if segments[0].heading() != 270:
#         segments[0].setheading(90)
# def down():
#     if segments[0].heading() != 90:
#         segments[0].setheading(270)

# screen.listen()
# screen.onkey(up, 'Up')
# screen.onkey(down, 'Down')
# screen.onkey(move_left, 'Left')
# screen.onkey(move_right, 'Right')

# game_on = True

# while game_on:
#     screen.update()
#     time.sleep(0.1)
#     for seg in range(len(segments) - 1, 0, -1):
#         x = segments[seg - 1].xcor()
#         y = segments[seg - 1].ycor()
#         segments[seg].goto(x, y)
#     segments[0].forward(20)

#     if segments[0].xcor() > 280 or segments[0].xcor() < -280 or segments[0].ycor() > 280 or segments[0].ycor() < -280:
#         game_on = False

# screen.exitonclick()