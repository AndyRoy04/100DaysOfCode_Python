from turtle import Turtle, Screen

jack = Turtle()
jack.shape("turtle")
jack.color('grey')

def move_turtle():
    jack.forward(200)
    jack.right(90)
    
for i in range(4):
    move_turtle()

my_screen = Screen()
my_screen.exitonclick()