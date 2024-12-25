from turtle import Turtle
ALIGNMENT = 'Center'
FONT = ("Courier", 14, "normal")

with open("100DaysOfCode_Python/Day_20_21/data.txt") as file_score:
    file_content = int(file_score.read())

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = file_content
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("100DaysOfCode_Python\Day_20_21\data.txt", mode='w') as new_high_score:
                new_high_score.write(str(self.high_score))
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()