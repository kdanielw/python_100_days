from turtle import Turtle
import random
NUMBER_OF_ANGLES = 4

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.starter_angle()

    def starter_angle(self):
        self.goto(0, 0)
        angle = 90 / random.randint(2, NUMBER_OF_ANGLES)
        quarter = random.randint(0, 3) * 90
        side = random.randint(0, 1) * 180
        final_angle = angle + quarter + side
        self.setheading(final_angle)
    
    def collision(self, orientation):
        if orientation == "horizontal":
            new_angle = 180 - self.heading()
        else:
            new_angle = 360 - self.heading()
            print(new_angle)
        self.setheading(new_angle)
