from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Futura", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        # self.shapesize()
        # self.speed("fastest")
        self.goto(0,270)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def accumulate_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False,ALIGNMENT, FONT)
