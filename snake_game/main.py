from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("darkslategray")
screen.title("Raupe Nimmersatt")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.place_food()
        snake.grow()
        score.update_score()

    # detect collision with food
    if not (-300 < snake.snake_head.xcor() < 300) or not (-300 < snake.snake_head.ycor() < 300):
        game_is_on = score.game_over()


    # detect collision with tail
    snake_tail = snake.snake_segments[1:]
    for segment in snake_tail:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = score.game_over()

screen.exitonclick()