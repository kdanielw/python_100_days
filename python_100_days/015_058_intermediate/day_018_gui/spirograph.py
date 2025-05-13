from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(5)
tim.speed("fastest")

screen = Screen()
screen.colormode(255)

def random_color():
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   return (r, g, b)

number_of_circles = 36

for i in range(number_of_circles):
    angle = i * (360 / number_of_circles)
    tim.setheading(angle)
    tim.color(random_color())    
    tim.circle(200)    
    
screen.exitonclick()
