import turtle
import pandas

FONT = ("Courier", 6, "normal")

def convert_coordenates(coord,axis):
    if axis == "y":
        coord = 2750 - coord
    new_coord = int(round(coord/5 - 550/2, 0))
    return new_coord

states_data = pandas.read_csv("states.csv")
all_states = states_data["state"].dropna().unique().tolist()
guessed_states = []


screen = turtle.Screen()
screen.title("Brasil State Game")
image = "brasil.gif"
screen.addshape(image)
screen.setup(width=550, height=550)

turtle.shape(image)

score = 0

while score < len(all_states):
    answer_state = screen.textinput(title=f"{score}/{len(all_states)} States Corrects", prompt="Whats is another state's name? ").lower()

    if answer_state == "exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in all_states:
        if answer_state == state.lower():
            guessed_states.append(state)
            x_coord = states_data[states_data.state == state].x.item()
            y_coord = states_data[states_data.state == state].y.item()

            new_x = convert_coordenates(x_coord,"x")
            new_y = convert_coordenates(y_coord,"y")
            position = (new_x, new_y)

            state_name = turtle.Turtle()
            state_name.hideturtle()
            state_name.penup()
            state_name.color("red")
            state_name.goto(position)
            state_name.write(state, align="center", font=FONT)
            score += 1
