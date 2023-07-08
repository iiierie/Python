import turtle as t

start_position = [0,-275]
step_size = 10

class Player(t.Turtle):
    def __init__(self,color):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.penup()
        self.goto(x = start_position[0], y = start_position[1])
        self.setheading(90)

    def move(self):
        self.fd(step_size)


    def restart(self):
        self.goto(x = start_position[0], y = start_position[1])