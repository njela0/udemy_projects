from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()


    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=1)

    def place_left_paddle(self, screen_width):
        self.goto(-((screen_width / 2) - 50) , 0)

    def place_right_paddle(self, screen_width):
        self.goto(((screen_width / 2) - 50), 0)