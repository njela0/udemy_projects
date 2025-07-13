from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellowgreen")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Helvetica", 20, "bold"))
        self.score += 1


