import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from board import SC_WIDTH, SC_HEIGHT

screen = Screen()
screen.colormode(255)
screen.setup(width=SC_WIDTH, height=SC_HEIGHT)
screen.bgcolor(0, 0, 0)
screen.title("Turtle Crossing")
screen.tracer(0)

# TODO => Create player object
player = Player()

# TODO => Create player movement
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.jump_right, "Right")
screen.onkey(player.jump_left, "Left")

# TODO => Create car behavior
# Car behavior is created through two methods, which are handled inside the 'CarManager' class:
# 1) gen_fleet => generates a fleet of cars using a specified number of cars
# 2) move_fleet => constantly moves each car inside the fleet
car_man = CarManager()
car_man.gen_fleet(24)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_man.move_fleet()
    screen.update()
