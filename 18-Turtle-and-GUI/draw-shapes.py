from turtle import Turtle, Screen

tim = Turtle()

tim.shape("arrow")
tim.color("red")


def triangle():
    tim.forward(60)
    for n in range(2):
        tim.left(120)
        tim.forward(60)


def square():
    tim.forward(60)
    for n in range(3):
        tim.left(90)
        tim.forward(60)


def pentagon():
    tim.forward(60)
    for n in range(4):
        tim.left(72)
        tim.forward(60)


def hexagon():
    tim.forward(60)
    for n in range(5):
        tim.left(60)
        tim.forward(60)


def heptagon():
    tim.forward(60)
    for n in range(6):
        tim.left(51.42)
        tim.forward(60)


def octagon():
    tim.forward(60)
    for n in range(7):
        tim.left(45)
        tim.forward(60)


def nonagon():
    tim.forward(60)
    for n in range(8):
        tim.left(40)
        tim.forward(60)


def decagon():
    tim.forward(60)
    for n in range(9):
        tim.left(36)
        tim.forward(60)


triangle()
tim.home()
square()
tim.home()
pentagon()
tim.home()
hexagon()
tim.home()
heptagon()
tim.home()
octagon()
tim.home()
nonagon()
tim.home()
decagon()
tim.home()

screen = Screen()
screen.exitonclick()
