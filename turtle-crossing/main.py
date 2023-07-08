import turtle as t
import time
from player import Player
from car_manager import car_manager
from scoreboard import Scoreboard

speed = 0.1

screen = t.Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.tracer(0)
screen.colormode(255)



player = Player("red")
car = car_manager()
scorebd= Scoreboard()




screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(speed)
    screen.update()

    car.create_cars()
    car.moves()


    #detect collision with car
    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            scorebd.game_over()



    # detect if player reached safety point across
    if player.ycor() > 280:
        player.restart()
        scorebd.score += 1
        scorebd.update()
        car.increase_speed()







screen.exitonclick()