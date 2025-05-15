from turtle import Turtle
import random
SCREEN_LIMIT = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("pink")
        self.speed("fastest")
        random_x = random.randint(-SCREEN_LIMIT, SCREEN_LIMIT)
        random_y = random.randint(-SCREEN_LIMIT, SCREEN_LIMIT)
        self.goto(x = random_x, y = random_y)
    
    def refresh(self):
        random_x = random.randint(-SCREEN_LIMIT, SCREEN_LIMIT)
        random_y = random.randint(-SCREEN_LIMIT, SCREEN_LIMIT)
        self.goto(x = random_x, y = random_y)
