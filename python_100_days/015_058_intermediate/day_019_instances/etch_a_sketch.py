from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_fowards():
    tim.forward(10)

def move_backwards():
    tim.forward(-10)

def clockwise():
    tim.setheading(tim.heading() - 10)

def counter_clockwise():
    tim.setheading(tim.heading() + 10)

def clear():
    screen.reset()    

screen.listen()

screen.onkey(key="w", fun=move_fowards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
