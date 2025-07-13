from turtle import Turtle
from colors import COLORS_FOOD
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.place_food()

    def place_food(self):
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 260)
        self.color(random.choice(COLORS_FOOD))
        self.goto(random_xcor, random_ycor)
