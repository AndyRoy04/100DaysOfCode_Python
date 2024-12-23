from turtle import Turtle
ALIGNMENT = 'Center'
FONT = ("Courier", 14, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.total = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.write(f"Score : {self.total}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! Final Score: {self.total}", align=ALIGNMENT, font=FONT)

    def score(self):
        self.clear()
        self.total += 1
        self.update()