import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

scoreboard.levelUp



screen.onkeypress(player.move, "Up")
game_is_on = True
carmanager = CarManager()


def collision():
    global game_is_on
    for everyCar in carmanager.cars:
        if player.distance(everyCar) < 20:
            scoreboard.gameOver()
            game_is_on = False

while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.createCar()
    carmanager.move()

    if player.ycor() == 280:
        scoreboard.levelUp()
        player.win()
        carmanager.win()

    collision()





screen.exitonclick()


