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

        self.segments = []        
        self.create_paddle()
        self.head = self.segments[0]
    
    def create_paddle(self):
        y_cord = (PADDLE_SEGMENTS / 2 - 1) * PADDLE_DIMENSIONS
        for _ in range(PADDLE_SEGMENTS):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            position = (0, y_cord)
            new_segment.goto(position)
            self.segments.append(new_segment)
            y_cord -= PADDLE_DIMENSIONS
    
    def choose_player(self, player):
        if player == 1:
            x_cord = -(X_LIMIT) - 10
        elif player == 2:
            x_cord = X_LIMIT
        for segment in self.segments:
            segment.goto(x = x_cord, y = segment.ycor())
    
    def move(self, direction):
        for segment in self.segments:
            new_y = segment.ycor() + PADDLE_DIMENSIONS * direction
            segment.goto(x = segment.xcor(), y = new_y)

    def up(self):
        if self.segments[0].ycor() < SCREEN_DIMENSION / 2 - PADDLE_DIMENSIONS:
            self.move(1)
    
    def down(self):
        if self.segments[-1].ycor() > -SCREEN_DIMENSION / 2 + PADDLE_DIMENSIONS:
            self.move(-1)