from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(-220, 260)
        self.color("black")
        self.write(f"Level: {self.level}", True, align=("center"), font=FONT)

    def levelUp(self):
        self.clear()
        self.level+=1
        self.update()

    def gameOver(self):
        self.goto(0, -150)
        self.color("black")
        self.write("Game over", True, align=("center"), font=FONT)