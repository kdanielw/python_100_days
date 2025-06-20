from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:   

    def __init__(self):
        self.snake = []        
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):       
        x_cord = 0
        y_cord = 0
        square_dimensions = MOVE_DISTANCE

        for _ in range(3):
            self.add_segment((x_cord, y_cord))
            x_cord -= square_dimensions            
        self.snake[0].color("red")
    
    def add_segment(self, position):        
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)        
        self.snake.append(new_segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())
    
    def move(self):
        for seg_number in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_number - 1].xcor()
            new_y = self.snake[seg_number - 1].ycor()
            self.snake[seg_number].goto(x = new_x, y = new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
            