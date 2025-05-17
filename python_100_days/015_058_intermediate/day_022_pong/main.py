from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_LIMIT = 380
SCREEN_DIMENSION = 800
SPEED_INCREASE = 2

def restart_game():
    paddle_l.sety = 0
    paddle_r.sety = 0
    ball.starter_angle()
    screen.update()
    global speed
    speed += SPEED_INCREASE
    time.sleep(2)

screen = Screen()
screen.setup(width=SCREEN_DIMENSION, height=SCREEN_DIMENSION)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
paddle_l = Paddle()
paddle_l.choose_player("l")
paddle_r = Paddle()
paddle_r.choose_player("r")

ball = Ball()

screen.listen()
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")

time.sleep(3)

wall_l = paddle_l.xcor() + 10
wall_r = paddle_r.xcor() - 10

speed = 10
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.forward(speed)

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
    if (ball.distance(paddle_l) <= 50 and ball.xcor() < wall_l) or (ball.distance(paddle_r) <= 50 and ball.xcor() > wall_r):
        ball.collision("horizontal")
        
screen.exitonclick()
