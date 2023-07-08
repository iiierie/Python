import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.update()

    def update(self):
        self.clear()  # Clear the previous score
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.write(f"Level: {self.score}", align="left", font=("Arial", 15, "normal"))

    def game_over(self):
        self.home()
        self.clear()
        self.write(f"GAME OVER! \n Final Score: {self.score}", align="center", font=("Arial", 20, "bold"))

