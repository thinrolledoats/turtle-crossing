from turtle import Turtle
from board import SC_UNIT, SC_WIDTH, SC_HEIGHT
import random

COLORS = [(242, 233, 228), (201, 173, 167), (154, 140, 152), (74, 78, 105)]
START_MOVE_DIST = SC_UNIT / 4


class CarManager:
    def __init__(self):
        # TODO => Create an empty list 'fleet', which will later store a number of 'cars'
        self.fleet = []

    def gen_fleet(self, num_of_cars):
        for car in range(num_of_cars):
            self.add_car()

    def add_car(self):
        # TODO => Create a car object using the 'Turtle' class
        #  Car shape should be a rectangle (use a square shape and shapesize() method to adjust the shape further)
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(SC_UNIT / 10, SC_UNIT / 20)
        new_car.color(random.choice(COLORS))
        new_car.setheading(90)
        new_car.goto(self.gen_random_pos())
        # TODO => Add the car object to the 'fleet' list
        self.fleet.append(new_car)

    def move_fleet(self, move_increment):
        for car in self.fleet:
            # TODO => Move the 'car' by a variable amount in the 'X' direction
            #  Move speed increases each level by a constant amount
            car.goto(car.xcor() - START_MOVE_DIST - move_increment, car.ycor())
            # TODO => Move the 'car' to the other end of the screen, if it reaches the 'X' boundary
            if car.xcor() < -SC_WIDTH:
                car.goto(car.xcor() * -1, self.gen_random_pos()[1])

    # TODO => Create a method that clears the entire existing 'fleet' and generates a new one
    def reset_fleet(self):
        for car in self.fleet:
            car.goto(self.gen_random_pos())

    # TODO => Create a method that checks the 'player' collision with a 'car'
    def check_col(self, turtle):
        for car in self.fleet:
            if car.distance(turtle) <= SC_UNIT:
                return 1
        return 0

    @staticmethod
    def gen_random_pos():
        x_rand = random.uniform(-SC_WIDTH, SC_WIDTH)
        y_rand = random.uniform(-(SC_HEIGHT / 2) + SC_UNIT * 3, (SC_HEIGHT / 2) - SC_UNIT * 3)
        random_pos = (x_rand, y_rand)
        return random_pos



