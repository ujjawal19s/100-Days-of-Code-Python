from turtle import Turtle, Screen
import pandas

turtle = Turtle()

screen = Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
score = 0
correct_guesses = []
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50  Guess the state", prompt="What's the another state name?")
    answer_state = answer_state.title()
    for state in all_states:
        if answer_state == "Exit":
            score = 51
            break
        if state == answer_state and correct_guesses.count(state) == 0:
            correct_guesses.append(answer_state)
            state_data = data[data.state == answer_state]
            t = Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(state_data.x), int(state_data.y))
            t.write(f"{answer_state}")
            score += 1

missed_states = []
for state in all_states:
    if correct_guesses.count(state) == 0:
        missed_states.append(state)

new_data = pandas.DataFrame(missed_states)

new_data.to_csv("learn.csv")
