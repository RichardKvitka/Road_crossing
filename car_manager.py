from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STARTING_POSITION = (300, random.randint(-250, 250))


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.acceleration = 0

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setposition(300, random.randint(-250, 250))
        new_car.color(random.choice(COLORS))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + self.acceleration)
