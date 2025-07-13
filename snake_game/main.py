import turtle
from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    turtle.onkeypress(snake.turn_left(), "Left")
    turtle.onkeypress(snake.turn_right(), "Right")

    screen.listen()


screen.exitonclick()