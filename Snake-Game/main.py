import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# create a black screen of 600x600 pixels
screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # used to on and off animations  # used along with screen.update()


my_snake = Snake()

food = Food()
food.refresh()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(my_snake.move_left, key = "Left")
screen.onkey(my_snake.move_right, key = "Right")
screen.onkey(my_snake.up,key = "Up")
screen.onkey(my_snake.down,key = "Down")


##until game ends keep moving snake forwards

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # time delay #controls the speed
    my_snake.move_forward()


    #detect food collission
    if my_snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        my_snake.extend_snake()


    # scoreboard
    if my_snake.snake_head.xcor() > 290 or my_snake.snake_head.xcor() < -290 or my_snake.snake_head.ycor() < -290 or  my_snake.snake_head.ycor() > 290:
        # game_is_on = False
        # scoreboard.gameover()
        scoreboard.reset()
        my_snake.reset()

    # detect tail collission

    for segment in my_snake.all_segments[1:]:

        if my_snake.snake_head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.gameover()
            scoreboard.reset()
            my_snake.reset()



screen.exitonclick()