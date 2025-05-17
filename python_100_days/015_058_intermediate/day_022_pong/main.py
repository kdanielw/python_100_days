from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_LIMIT = 380
SCREEN_DIMENSION = 800

def restart_game():
    paddle_1.sety = 0
    paddle_2.sety = 0
    ball.starter_angle()
    screen.update()
    time.sleep(2)

screen = Screen()
screen.setup(width=SCREEN_DIMENSION, height=SCREEN_DIMENSION)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
paddle_1 = Paddle()
paddle_1.choose_player(1)
paddle_2 = Paddle()
paddle_2.choose_player(2)

ball = Ball()

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")


time.sleep(3)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.forward(10)

    # Ball vertical collison
    if ball.ycor() >= SCREEN_LIMIT or ball.ycor() <= -SCREEN_LIMIT:
        ball.collision("vertical")

    # Goals    
    if ball.xcor() < -SCREEN_DIMENSION / 2:
        game_is_on = scoreboard.inscrease_score(2)
        restart_game()
    if ball.xcor() > SCREEN_DIMENSION / 2:
        game_is_on = scoreboard.inscrease_score(1)
        restart_game()

    # Ball collision with paddle
    for segment in range (len(paddle_1.segments)):
        if ball.distance(paddle_1.segments[segment]) <= 20 or ball.distance(paddle_2.segments[segment]) <= 20:
            ball.collision("horizontal")
    

        

screen.exitonclick()
