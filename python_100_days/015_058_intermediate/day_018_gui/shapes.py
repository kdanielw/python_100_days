from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

screen = Screen()
screen.colormode(255)
screen.screensize(750, 750)

def random_color():
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   return (r, g, b)

sides_number = 3

for _ in range(3, 11):
    angle = 360 / sides_number
    for _ in range(sides_number):
        tim.forward(100)
        tim.right(angle)
    sides_number += 1
    tim.color(random_color())

screen.exitonclick()
