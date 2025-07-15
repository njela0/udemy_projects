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

screen.listen()
screen.onkeypress(paddle_left.upwards, "w")
screen.onkeypress(paddle_left.downwards, "s")
screen.onkeypress(paddle_right.upwards, "Up")
screen.onkeypress(paddle_right.downwards, "Down")


game_is_on = True

while game_is_on:
    screen.update()



screen.exitonclick()