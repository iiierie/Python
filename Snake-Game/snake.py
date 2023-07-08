import turtle as t
up = 90
down = 270
left = 180
right = 0
class Snake:
    #initialize variables
    def __init__(self):
        #attributes
        self.all_segments = []
        #method to create snake
        self.make_snake()
        self.snake_head = self.all_segments[0]



    def add_segment(self,i):
        turt = t.Turtle(shape="circle")
        # turt.shapesize(stretch_wid=0.5, stretch_len= 1)
        turt.penup()
        turt.color("white")
        x_coord = 0 - i * 20
        turt.goto(x=x_coord, y=0)
        self.all_segments.append(turt)



    #create a snake using three square turtles
    def make_snake(self):
        for i in range(3): #creates three turtles joined together to make it look like a snake
            self.add_segment(i);

    #function to make snake keep moving forward
    # logic : simply move segment 3 to segment 2 , segment 2 to segment 1 and segment 1 forward
    def move_forward(self):
            total_segments = len(self.all_segments)
            for i in range(total_segments - 1, 0, -1): # 3,2,1
                new_x_position = self.all_segments[i - 1].xcor()
                new_y_position = self.all_segments[i - 1].ycor()
                self.all_segments[i].goto(new_x_position, new_y_position)
            self.all_segments[0].fd(20)


    # user control functions for onkey command
    def move_left(self):
        if self.all_segments[0].heading() != right:
            self.snake_head.setheading(left)

    def move_right(self):
        if self.all_segments[0].heading() != left:
            self.snake_head.setheading(right)

    # if snake is moving up, it cannot reverse its path down and vice-versa so check conditions
    def up(self):
        if self.all_segments[0].heading()!= down:
            self.snake_head.setheading(up)

    def down(self):
        if self.all_segments[0].heading() != up:
            self.snake_head.setheading(down)


    def reset(self):
        for segment in self.all_segments:
            segment.goto(1000,1000)
        self.all_segments.clear()
        self.make_snake()
        self.snake_head = self.all_segments[0]


    def extend_snake(self):
        self.add_segment(self.all_segments[-1].position()[0])