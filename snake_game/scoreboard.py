from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

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
        """Updates the score on the screen."""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1


    def game_over(self):
        """Writes "Game Over"-Message in the middle of the screen and returns False."""
        self.goto(0, 0)
        self.pencolor("orangered")
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

        return False