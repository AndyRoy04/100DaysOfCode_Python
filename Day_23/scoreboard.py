from turtle import Turtle
FONT = ("Comic Sans", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f'Level : {self.score}', align='left', font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f'Level : {self.score}', align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('grey')
        self.write(f'Game Over! Final Score: {self.score}', align='center', font=("Comic Sans", 18, "bold"))
