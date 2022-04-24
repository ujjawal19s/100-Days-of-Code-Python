from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def clockwise():
    tim.right(10)


def anti_clockwise():
    tim.left(10)


screen.listen()
screen.onkey(move_forward, "W")
screen.onkey(move_backward, "S")
screen.onkey(clockwise, "D")
screen.onkey(anti_clockwise, "A")
screen.onkey(clear_drawing, "C")
screen.exitonclick()
