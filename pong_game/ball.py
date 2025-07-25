from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction = 10
        self.y_direction = 10
        self.ball_speed = 0.1


    def move(self):
        """Moves the ball."""
        new_xcor = self.xcor() + self.x_direction
        new_ycor = self.ycor() + self.y_direction
        self.goto(new_xcor, new_ycor)


    def speed_up(self):
        """Enhances the speed of the ball."""
        self.ball_speed *= 0.9


    def speed_reset(self):
        """Resets the speed of the ball."""
        self.ball_speed = 0.1


    def x_bounce(self):
        """Changes the y-direction of the ball."""
        self.y_direction *= - 1
        self.speed_up()


    def y_bounce(self):
        """Changes the x-direction of the ball."""
        self.x_direction *= -1


    def position_reset(self):
        """Resets the position of the ball."""
        self.home()
        self.speed_reset()



