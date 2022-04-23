import turtle as t

import random
tim = t.Turtle()
t.colormode(255)
color_list = [(236, 235, 240), (236, 231, 234), (222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205), (223, 178, 169)]
tim.shape("arrow")
tim.speed(0)
tim.hideturtle()
tim.left(225)
tim.penup()
tim.forward(300)
tim.right(225)
tim.pendown()

for dot_count in range(1, 101):
    tim.color(random.choice(color_list))
    tim.dot(20)
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if dot_count%10== 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


my_screen = t.Screen()
my_screen.exitonclick()
