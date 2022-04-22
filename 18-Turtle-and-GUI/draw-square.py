from turtle import Turtle, Screen

tim = Turtle()

tim.shape("arrow")
tim.color("black")

for n in range(4):
    tim.forward(100)
    tim.left(90)

screen = Screen()
screen.exitonclick()
