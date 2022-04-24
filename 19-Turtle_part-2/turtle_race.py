from turtle import Turtle, Screen
import random

is_game_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
color = ["red", "orange", "black", "green", "brown", "blue"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle in range(0, 6):
    tim = Turtle()
    tim.shape("turtle")
    tim.color(color[turtle])
    tim.penup()
    tim.goto(x=-230, y=y_pos[turtle])
    all_turtle.append(tim)


if user_bet:
    is_game_on = True

while is_game_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"The winner is {winning_color}, You won the game")
            else:
                print(f"The winner is {winning_color}, You lost the game")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
