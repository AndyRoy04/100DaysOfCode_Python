from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def left_score(self):
        self.goto(-100, 200)
        self.speed('fastest')
        self.write(self.l_score, align='center', font=('Comic Sans', 50, 'bold'))
    
    def right_score(self):
        self.goto(100, 200)
        self.speed('fastest')
        self.write(self.r_score, align='center', font=('Comic Sans', 50, 'bold'))