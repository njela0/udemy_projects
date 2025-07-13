import turtle
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_segments = []

for _ in range(3):
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    snake_segments.append(new_segment)


for index, segment in enumerate(snake_segments):
    if index < len(snake_segments) - 1:

        x_cor = segment.xcor()
        y_cor = segment.ycor()

        snake_segments[index+1].teleport(x_cor - 20, y_cor)


game_is_on = True


def move_snake():
    for segment_num in range((len(snake_segments) - 1), 0, -1):
        x_cor_new = snake_segments[segment_num - 1].xcor()
        y_cor_new = snake_segments[segment_num - 1].ycor()

        snake_segments[segment_num].goto(x_cor_new, y_cor_new)

    snake_segments[0].forward(20)

def turn_left():
    snake_segments[0].left(90)

def turn_right():
    snake_segments[0].right(90)


while game_is_on:
    screen.update()
    time.sleep(0.1)

    move_snake()

    turtle.onkeypress(turn_left, "Left")
    turtle.onkeypress(turn_right, "Right")
    screen.listen()




screen.exitonclick()