from turtle import Turtle, Screen
import random
tim = Turtle()

tim.shape("arrow")
color = ["red", "yellow", "orange", "green", "black", "blue", "brown"]
directions = [0, 90, 180, 270]
tim.speed(0)
tim.width(10)
for n in range(200):
    tim.color(random.choice(color))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
