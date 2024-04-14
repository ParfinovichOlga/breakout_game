from turtle import Turtle
START_X = -370
START_Y = 180
COLORS = ['red', 'orange', 'green', 'yellow']
#COLORS = ['red']

class Brick (Turtle):
    def __init__(self):
        super().__init__()
        self.start_x = START_X
        self.start_y = START_Y
        self.shift = 56
        self.hideturtle()
        self.speed(0)
        self.all_bricks = []

    def create_color_rows(self):
        for color in COLORS:
            for i in range(2):
                for n in range(14):
                    brick = Turtle(shape='square')
                    brick.shapesize(stretch_len=2.5, stretch_wid=0.7)
                    brick.color(color)
                    brick.penup()
                    brick.goto(self.start_x, self.start_y)
                    self.all_bricks.append(brick)
                    self.start_x += self.shift
                self.start_y -= self.shift/3
                self.start_x = START_X


