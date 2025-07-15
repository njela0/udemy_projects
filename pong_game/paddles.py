from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.goto(self.x_cor, self.y_cor)

    def upwards(self):
        """Moves the paddle upwards."""
        new_ycor = self.ycor() + 20
        if -250 < new_ycor < 250:
            self.goto(self.xcor(), new_ycor)


    def downwards(self):
        """Moves the paddle downwards."""
        new_ycor = self.ycor() - 20
        if -250 < new_ycor < 250:
            self.goto(self.xcor(), new_ycor)

