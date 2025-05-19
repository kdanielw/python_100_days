from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_LIMIT = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

time.sleep(3)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.inscrease_score()
        snake.extend()
    
    #Detect collision with wall
    if snake.head.xcor() > SCREEN_LIMIT or snake.head.xcor() < -SCREEN_LIMIT or snake.head.ycor() > SCREEN_LIMIT or snake.head.ycor() < -SCREEN_LIMIT:
        scoreboard.reset()
        snake.reset()
    
    #Detect collision with body
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

        

screen.exitonclick()
