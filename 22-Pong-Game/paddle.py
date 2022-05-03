from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor,y_cor)

    def go_up(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)

    def go_down(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)






