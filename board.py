from turtle import Turtle

SC_UNIT = 20
XR_FACTOR = 6
YR_FACTOR = 3
SC_WIDTH = SC_UNIT * XR_FACTOR * 10
SC_HEIGHT = SC_UNIT * YR_FACTOR * 10
FONT = ('FFF Forward', int(SC_UNIT), 'normal')
ALIGNMENT = 'left'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(255, 255, 255)
        self.hideturtle()
        self.level = 1
        self.print_level()

    # TODO => Create a method that prints current level
    def print_level(self):
        self.goto(-(SC_WIDTH / 2) + SC_UNIT, (SC_HEIGHT / 2) - SC_UNIT * YR_FACTOR)
        self.write(f"LEVEL: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    # TODO => Create a method that increments current level by 1, clears the screen and reprints the level
    def update_level(self):
        self.level += 1
        self.clear()
        self.print_level()

    # TODO => Create a method that prints 'GAME OVER'
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align='center', font=FONT)
