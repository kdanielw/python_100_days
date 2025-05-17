import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

Y_LIMIT = 280
CAR_DENSITY = 10

def next_level():
    global car_manager
    car_manager.increase_difficult()
    player.sety(-Y_LIMIT)


# Building the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Street")
screen.tracer(0)

# Building the scoreboard
scoreboard = Scoreboard()

# Building the player
player = Player()

car_manager = CarManager(CAR_DENSITY)

screen.listen()
screen.onkey(player.move, "Up")

time.sleep(3)

speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    car_manager.move_cars()

    if player.ycor() >= Y_LIMIT:
        scoreboard.level_up()
        next_level()
    
    for line in car_manager.car_matrix:
        for car in line:
            if player.distance(car) < 20:
                game_is_on = scoreboard.game_over()

screen.exitonclick()
