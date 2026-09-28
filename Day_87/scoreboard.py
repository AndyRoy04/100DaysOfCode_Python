from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(270, 310)
        self.display()
        
    def display(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Consolas", 14, "bold"))
        
    def increment(self):
        self.score += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 30, "bold"))

    def you_win(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=("Arial", 30, "bold"))