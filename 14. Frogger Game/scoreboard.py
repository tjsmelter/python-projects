# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-190,250)
        self.write(f"Level: {self.level}",align="center", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,align="center",font=FONT)
