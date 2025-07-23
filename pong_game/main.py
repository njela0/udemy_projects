from turtle import Screen
from paddles import Paddle
from pong_game.ball import Ball
from scoreboard import Scoreboard
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

# initialise the scoreboard
score = Scoreboard()

# draw the line
line = Scoreboard()
line.draw_line()
screen.update()


# start the game
game_is_on = True

x_direction = 10
y_direction = 10

while game_is_on:
    score.update_scoreboard()
    screen.update()
    time.sleep(ball.ball_speed)


    # detect collision with wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.x_bounce()


    # detect collision with paddle
    if  ball.distance(paddle_left) < 60 and ball.xcor() < -320:
        ball.y_bounce()


    if ball.distance(paddle_right) < 60 and ball.xcor() > 320:
        ball.y_bounce()


    # detect if ball is out of bounds
    if ball.xcor() < -360:
        score.score_right += 1
        ball.y_bounce()
        ball.position_reset()
        time.sleep(0.3)


    if ball.xcor() > 360:
        score.score_left += 1
        ball.y_bounce()
        ball.position_reset()
        time.sleep(0.3)


    ball.move()

screen.exitonclick()