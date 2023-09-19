import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from board import Scoreboard, SC_WIDTH, SC_HEIGHT

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
#  The behavior is achieved through two methods, which are handled inside the 'CarManager' class:
#  1) gen_fleet => generates a fleet of cars using a specified number of cars
#  2) move_fleet => constantly moves each car inside the fleet
car_fleet = CarManager()
car_fleet.gen_fleet(24)

# TODO => Create a scoreboard
score = Scoreboard()

move_increment = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_fleet.move_fleet(move_increment)
    # TODO => Create a game reset functionality
    #  The functionality should be used when the player reaches a new level
    # IF reset has returned 0, the player will LEVEL UP
    if player.reset_pos() == 0:
        # 1) Reset car fleet
        car_fleet.reset_fleet(24)
        # 2) Update level (+1)
        score.update_level()
        # 3) Increment the movement speed
        move_increment += 10
    # IF the collision check has returned 1, the player will LOSE
    if car_fleet.check_col(player) == 1:
        game_is_on = False
    screen.update()
screen.exitonclick()
