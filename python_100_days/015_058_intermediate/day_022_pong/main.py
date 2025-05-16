# ball
# paddle
# scoreboard

from turtle import Screen
from paddle import Paddle
import time

SCREEN_LIMIT = 380
SCREEN_DIMENSION = 800

screen = Screen()
screen.setup(width=SCREEN_DIMENSION, height=SCREEN_DIMENSION)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle()
paddle_1.choose_player(1)

paddle_2 = Paddle()
paddle_2.choose_player(2)

# ball = Ball()
# scoreboard = Scoreboard()

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
        

screen.exitonclick()
