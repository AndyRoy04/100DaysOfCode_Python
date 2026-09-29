from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.hideturtle()
        self.penup()
        self.color('white')
        self.display()
        
    def display(self):
        self.clear()
        self.goto(-320, 320)
        self.write(f"Score: {self.score}", font=("Courier", 14, "bold"))
        self.goto(200, 320)
        self.write(f"Lives: {'♥ ' * self.lives}", font=("Courier", 13, "bold"))
        
    def increment(self):
        self.score += 1
        self.display()
        
    def lose_life(self):
        self.lives -= 1
        self.display()
        return self.lives

    def big_message(self, msg, color):
        self.goto(0, 0)
        self.color(*color)
        self.write(msg, align="center", font=("Courier", 32, "bold"))

    def you_win(self):
        self.big_message("YOU WIN!", (57, 255, 20))

    def game_over(self):
        self.big_message("GAME OVER", (247, 66, 31))
