from turtle import Screen
from paddles import Paddle

# set constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# set up the screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create left and right paddle as instance of the paddle class
paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)

# set the events for paddle movement
screen.listen()
screen.onkeypress(paddle_left.upwards, "w")
screen.onkeypress(paddle_left.downwards, "s")
screen.onkeypress(paddle_right.upwards, "Up")
screen.onkeypress(paddle_right.downwards, "Down")

# start the game
game_is_on = True

while game_is_on:
    screen.update()



screen.exitonclick()