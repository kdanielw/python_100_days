from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(10)
tim.speed("fastest")

screen = Screen()
screen.colormode(255)

def random_color():
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   return (r, g, b)

for _ in range(200):
    tim.color(random_color())
    angle = random.randint(1, 4) * 90
    tim.forward(50)
    tim.setheading(angle)
    
screen.exitonclick()