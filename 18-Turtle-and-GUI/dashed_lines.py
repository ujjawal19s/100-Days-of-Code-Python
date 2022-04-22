from turtle import Turtle, Screen

tim = Turtle()

tim.shape("arrow")
tim.color("black")

for n in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()
