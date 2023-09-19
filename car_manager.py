from turtle import Turtle
from board import SC_UNIT, SC_WIDTH, SC_HEIGHT
import random

COLORS = []
START_MOVE_DIST = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        # TODO => Create an empty list 'fleet', which will later store a number of 'cars'
        self.fleet = []

    def gen_fleet(self, num_of_cars):
        for car in range(num_of_cars):
            self.add_car()

    def add_car(self):
        # TODO => Create a car object using the 'Turtle' class
        # Car shape should be a rectangle (use a square shape and shapesize() method to adjust the shape further)
        new_car = Turtle("square")
        new_car.shapesize(2, 1)
        new_car.color(229, 229, 229)
        new_car.setheading(90)
        new_car.penup()
        start_pos_rand = self.gen_random_pos()
        new_car.goto(start_pos_rand)
        # TODO => Add the car object to the 'fleet' list
        self.fleet.append(new_car)

    def move_fleet(self):
        for car in self.fleet:
            # TODO => Move the 'car' by a constant amount in the 'X' direction
            car.goto(car.xcor() - START_MOVE_DIST, car.ycor())
            # TODO => Move the 'car' to the other end of the screen, if it reaches the 'X' boundary
            if car.xcor() < -SC_WIDTH:
                car.goto(car.xcor() * -1, self.gen_random_pos()[1])

    @staticmethod
    def gen_random_pos():
        x_rand = random.uniform(-SC_WIDTH, SC_WIDTH)
        y_rand = random.uniform(-(SC_HEIGHT / 2), (SC_HEIGHT / 2))
        random_pos = (x_rand, y_rand)
        return random_pos



