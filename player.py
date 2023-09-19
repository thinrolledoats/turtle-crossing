from turtle import Turtle
from board import SC_UNIT, SC_HEIGHT
START_POS = (0, -((SC_HEIGHT / 2) - SC_UNIT))
MOVE_DIST = 10
JUMP_DIST = MOVE_DIST * 2
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(255, 255, 255)
        self.setheading(90)
        self.penup()
        self.goto(START_POS)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DIST)

    def jump_right(self):
        self.goto(self.xcor() + JUMP_DIST, self.ycor())

    def jump_left(self):
        self.goto(self.xcor() - JUMP_DIST, self.ycor())

    # TODO => Create a method that resets the 'player' position once they reach the top of the screen
    #  The method should return 0 if it has successfully returned the 'player' to the starting position
    def reset_pos(self):
        if self.ycor() >= SC_HEIGHT / 2:
            self.goto(START_POS)
            return 0
        return 1


