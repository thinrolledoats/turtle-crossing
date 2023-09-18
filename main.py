import time
from turtle import Screen
from board import SC_WIDTH, SC_HEIGHT

screen = Screen()
screen.colormode(255)
screen.setup(width=SC_WIDTH, height=SC_HEIGHT)
screen.title("Turtle Crossing")
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
