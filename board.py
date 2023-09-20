from turtle import Turtle

SC_UNIT = 20
XR_FACTOR = 6
YR_FACTOR = 3
SC_WIDTH = SC_UNIT * XR_FACTOR * 10
SC_HEIGHT = SC_UNIT * YR_FACTOR * 10
FONT = ('FFF Forward', int(SC_UNIT), 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(255, 255, 255)
        self.hideturtle()
        self.level = 1
        self.print_level()
        # TODO => Create a 'high score' feature
        #  The method should store the 'high score' inside a text file
        with open('high_score.txt', mode="r") as file:
            self.high_score = int(file.read())
        self.print_high_score()

    # TODO => Create a method that prints current level
    def print_level(self):
        self.goto(-(SC_WIDTH / 2) + SC_UNIT, (SC_HEIGHT / 2) - SC_UNIT * YR_FACTOR)
        self.write(f"LEVEL: {self.level}", move=False, align='left', font=FONT)

    # TODO => Create a method that prints the high score
    #  The method should update the text file if there is a new 'high score'
    def print_high_score(self):
        if self.level > self.high_score:
            self.high_score = self.level - 1
            with open('high_score.txt', mode="w") as file:
                file.write(str(self.high_score))
        self.goto((SC_WIDTH / 2) - SC_UNIT, (SC_HEIGHT / 2) - SC_UNIT * YR_FACTOR)
        self.write(f"HIGH: {self.high_score}", move=False, align='right', font=FONT)

    # TODO => Create a method that increments current level by 1, clears the screen and reprints the level
    def update_board(self):
        self.level += 1
        self.clear()
        self.print_level()
        self.print_high_score()

    # TODO => Create a method that prints 'GAME OVER'
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align='center', font=FONT)
