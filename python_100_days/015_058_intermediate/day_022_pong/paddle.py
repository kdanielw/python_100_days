from turtle import Turtle

PADDLE_SEGMENTS = 5
PADDLE_DIMENSIONS = 20
PADDLE_HEIGHT = PADDLE_SEGMENTS * PADDLE_DIMENSIONS
SCREEN_DIMENSION = 800
X_LIMIT = SCREEN_DIMENSION / 2 - PADDLE_DIMENSIONS
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len = 1, stretch_wid = PADDLE_SEGMENTS)
        self.penup()
        self.color("white")
    
    def choose_player(self, player):
        if player == "l":
            x_cord = -(X_LIMIT) + 20
        elif player == "r":
            x_cord = X_LIMIT -20
        self.goto(x = x_cord, y = self.ycor())
    
    def move(self, direction):
        new_y = self.ycor() + PADDLE_DIMENSIONS * direction
        self.goto(x = self.xcor(), y = new_y)

    def up(self):
        if self.ycor() < SCREEN_DIMENSION / 2 - PADDLE_DIMENSIONS:
            self.move(1)
    
    def down(self):
        if self.ycor() > -SCREEN_DIMENSION / 2 + PADDLE_DIMENSIONS:
            self.move(-1)
