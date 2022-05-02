from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.increase_speed()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def increase_speed(self):
        self.score += 1
        self.clear()
        self.update_score()
