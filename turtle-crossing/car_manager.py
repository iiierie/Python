import turtle as t
import random



class car_manager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 15

    def generate_random_rgb(self):
        r = random.randint(1,255)
        g = random.randint(1, 255)
        b = random.randint(1 , 255)
        new_color = (r,g,b)
        return new_color

    def create_cars(self):
        random_int = random.randint(1,4)
        if random_int == 2:
            new_car = t.Turtle("square")
            new_car.penup()
            car_width = 1
            car_length = random.randint(1, 3)
            x = random.randint(-250, 250)
            new_car.color(self.generate_random_rgb())
            y = random.randint(-250, 250)
            new_car.goto(300,y)
            new_car.shapesize(stretch_wid=car_width, stretch_len=car_length)
            self.all_cars.append(new_car)



    def moves(self):
        for car in self.all_cars:
            car.setheading(180)
            car.fd(self.car_speed)

    def increase_speed(self):
        self.car_speed += 10

