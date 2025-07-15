"""
classes - paddles, ball, scoreboard
"""
from turtle import Screen

from paddles import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_left = Paddle()
paddle_right = Paddle()

paddle_left.place_left_paddle(SCREEN_WIDTH)
paddle_right.place_right_paddle(SCREEN_WIDTH)

screen.update()

screen.exitonclick()