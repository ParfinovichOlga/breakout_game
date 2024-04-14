from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from bricks import Brick
from scoreboard import Scoreboard

STARTING_POSITION = (0, -275)
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)
screen.listen()


def start_breakout_game():
    bricks = Brick()
    paddle = Paddle(STARTING_POSITION)
    ball = Ball()
    scoreboard = Scoreboard()
    scoreboard.update_score()
    screen.onkey(paddle.go_left, "Left")
    screen.onkey(paddle.go_right, "Right")
    bricks.create_color_rows()
    game_is_on = True
    game = 2
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()
        if len(bricks.all_bricks) == 0:
            game -= 1
            if game > 0:
                bricks.create_color_rows()
                paddle.goto(STARTING_POSITION)
                ball.reset_position()
        # Detect collision with brick
        for brick in bricks.all_bricks:
            if ball.distance(brick) < 50:
                color = brick.color()[0]
                if color == 'yellow':
                    scoreboard.yellow_point()
                elif color == 'green':
                    scoreboard.green_point()
                elif color == 'orange':
                    scoreboard.orange_point()
                    if ball.move_speed > 0.09:
                        ball.move_speed = 0.001
                elif color == 'red':
                    scoreboard.red_point()
                    ball.move_speed = 0.0009
                scoreboard.update_score()
                ball.bounce_y()
                brick.reset()
                brick.clear()
                bricks.all_bricks.remove(brick)
        # Detect collision with paddle
        if ball.ycor() < -252.1 and ball.distance(paddle) < 150:
            if ball.towards(paddle) > 200:
                ball.bounce_left()
            else:
                ball.bounce_y()
        # Detect paddle misses
        if ball.ycor() < -275:
            time.sleep(2)
            scoreboard.miss_ball()
            if scoreboard.turn < 1:
                game_is_on = False
                scoreboard.end_game()
                screen.update()
            else:
                ball.reset_position()
            scoreboard.update_score()
        # Detect ball out X
        if ball.xcor() > 375 or ball.xcor() < -375:
            ball.bounce_x()
        # Detect ball out Y
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
    scoreboard.end_game()


def restart_game():
    screen.reset()
    start_breakout_game()


start_breakout_game()

screen.onkey(restart_game, 'Up')

screen.mainloop()













