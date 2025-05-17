from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_LINES = 7
SCREEN_LIMIT = 280
DISTANCE_OF_LINES = 30

class CarManager:

    def __init__(self, chance_of_car):
        self.car_matrix = []
        self.percent_car = chance_of_car
        self.speed = STARTING_MOVE_DISTANCE
        self.create_lines()
    
    def create_lines(self):
        y_cord = -200
        for _ in range(NUMBER_LINES):
            line = []
            random_space = random.randint(0, 25)
            x_cord = -SCREEN_LIMIT
            for _ in range(2500):
                car_or_not = random.randint(1, 100)
                if car_or_not <= self.percent_car:
                    new_car = Turtle("square")
                    new_car.penup()
                    new_car.shapesize(stretch_wid = 1, stretch_len=2)
                    new_car.color(random.choice(COLORS))
                    new_car.setheading(180)
                    new_x = x_cord - random_space
                    new_car.goto(new_x, y_cord)
                    line.append(new_car)
                x_cord += 20

            self.car_matrix.append(line)
            y_cord += DISTANCE_OF_LINES
    
    def move_cars(self):
        for line in self.car_matrix:
            for car in line:
                car.forward(self.speed)

    def increase_difficult(self):
        self.speed += MOVE_INCREMENT
