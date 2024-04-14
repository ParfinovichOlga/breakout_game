from turtle import Turtle
START_MOVE_SPEED = 0.07


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, -252)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = START_MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_left(self):
        if self.x_move < 0:
            self.y_move = self.y_move * -1
        else:
            self.bounce()

    def bounce(self):
        self.y_move = self.y_move * -1
        self.x_move = self.x_move * -1

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.move_speed = START_MOVE_SPEED
        self.goto(0, -252)
        self.bounce_y()


