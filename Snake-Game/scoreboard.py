import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt","r+") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x= 0, y = 270)
        self.update_score()
        self.hideturtle()

    def write_highscore(self):
        with open("highscore.txt","r+") as file:
            file.write(str(self.highscore))




    def increase_score(self):
        self.score += 1
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=('Calibri', 18, 'bold'))


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore()
        self.score = 0
        self.update_score()
