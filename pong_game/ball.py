from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction = 10
        self.y_direction = 10


    def move(self):
        """Moves the ball."""
        new_xcor = self.xcor() + self.x_direction
        new_ycor = self.ycor() + self.y_direction
        self.goto(new_xcor, new_ycor)


    def x_bounce(self):
        """Changes the y-direction of the ball."""
        self.y_direction *= - 1


    def y_bounce(self):
        """Changes the x-direction of the ball."""
        self.x_direction *= -1

