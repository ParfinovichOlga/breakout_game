from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.turn = 3

    def write_score(self):
        self.goto(300, 230)
        self.write(self.score, align="center", font=("Courier", 30, "normal"))

    def write_turns(self):
        self.goto(-375, 260)
        self.write(self.turn, align="center", font=("Courier", 15, "bold"))

    def update_score(self):
        self.clear()
        self.write_score()
        self.write_turns()

    def yellow_point(self):
        self.score = self.score + 1

    def green_point(self):
        self.score = self.score + 3

    def orange_point(self):
        self.score = self.score + 5

    def red_point(self):
        self.score = self.score + 7

    def miss_ball(self):
        self.turn -= 1

    def end_game(self):
        self.goto(0, -15)
        self.write(f'Your score: {self.score}\nPress ↑ to restart game', align="center", font=("Courier", 20, "normal"))
