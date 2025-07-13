from turtle import Turtle
from colors import colors_css
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(random.choice(colors_css))
        self.speed("fastest")
        self.place_food()

    def place_food(self):
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 260)
        self.goto(random_xcor, random_ycor)
