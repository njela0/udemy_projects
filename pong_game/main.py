from turtle import Screen
from paddles import Paddle
from pong_game.ball import Ball
import time


# set constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# set up the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# initialise left and right paddle as instance of the paddle class
paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)


# set the events for paddle movement
screen.listen()
screen.onkeypress(paddle_left.upwards, "w")
screen.onkeypress(paddle_left.downwards, "s")
screen.onkeypress(paddle_right.upwards, "Up")
screen.onkeypress(paddle_right.downwards, "Down")


# initialise the ball
ball = Ball()
screen.update()


# start the game
game_is_on = True

x_direction = 10
y_direction = 10

score_left = 0
score_right = 0

while game_is_on:

    screen.update()
    time.sleep(0.1)

    # detect collision with wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.wall_bounce()

    # detect collision with paddle
    if  ball.distance(paddle_left) < 60 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.distance(paddle_right) < 60 and ball.xcor() > 320:
        ball.paddle_bounce()

    if ball.xcor() < -380:
        score_right += 1
        ball.home()
        time.sleep(0.3)

    if ball.xcor() > 380:
        score_left += 1
        ball.home()
        time.sleep(0.3)

    ball.move()




screen.exitonclick()