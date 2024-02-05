from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()



    def createCar(self):
        randomChanse = random.randint(1,5)  # 1 in 5 chanse of creating car
        if randomChanse == 3:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(1, 2)
            car.left(180)
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)


    def move(self):
        for everyCar in self.cars:
            everyCar.forward(STARTING_MOVE_DISTANCE)


    def win(self):
       global STARTING_MOVE_DISTANCE
       STARTING_MOVE_DISTANCE += MOVE_INCREMENT