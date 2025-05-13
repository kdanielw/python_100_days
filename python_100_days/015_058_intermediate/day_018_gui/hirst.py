import colorgram
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(5)
tim.speed("fast")

screen = Screen()
screen.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_tuple = (r, g, b)
    rgb_colors.append(rgb_tuple)

for i in range(5):
    rgb_colors.remove(rgb_colors[0])

dots_per_line = 10
x_cord = 0
y_cord = 0
tim.penup()
tim.hideturtle()

for i in range(dots_per_line * dots_per_line):
    if i % dots_per_line == 0 and i != 0:        
        y_cord += 50
        x_cord = 0
        tim.setposition(x_cord, y_cord) 
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

screen.exitonclick()