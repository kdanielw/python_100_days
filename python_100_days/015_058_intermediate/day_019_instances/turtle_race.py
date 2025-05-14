from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_height = 150
space_betwen = starting_height / (len(colors) - 1)
all_turtles = []

for turtle_index in range(len(colors)):    
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    pos_y = -(starting_height / 2) + space_betwen * turtle_index
    new_turtle.goto(x=-230, y=pos_y)
    all_turtles.append(new_turtle)


user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race: Choose dthe color: ")

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!!!")
            else:
                print(f"You've lost! The {winning_color} is the winner!!!")
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
