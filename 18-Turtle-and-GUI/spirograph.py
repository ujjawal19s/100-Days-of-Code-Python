import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.shape("arrow")


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


directions = [0, 90, 180, 270]
tim.speed(0)

for n in range(int(360/5)):
    tim.color(color())
    tim.circle(100)
    tim.left(5)


my_screen = t.Screen()
my_screen.exitonclick()
