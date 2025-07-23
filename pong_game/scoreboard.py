from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")
LINE_DISTANCE = 20

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 240)
        self.score_left = 0
        self.score_right = 0


    def update_scoreboard(self):
        """Updates the shown scoreboard."""
        self.clear()
        self.write(f"{self.score_left} : {self.score_right}", align=ALIGNMENT, font=FONT)


    def draw_line(self):
        """Draws a line in the middle of the screen."""
        self.pensize(3)
        for _ in range(50):
            self.penup()
            self.goto(self.xcor(), self.ycor() - LINE_DISTANCE)
            self.pendown()
            self.goto(self.xcor(), self.ycor() - LINE_DISTANCE)