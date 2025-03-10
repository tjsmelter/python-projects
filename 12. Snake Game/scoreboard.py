# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Futura", 24, "normal")

class Scoreboard(Turtle):
    # initialize the scoreboard class that will set an attribute score to start at 0, the color, and position on the screen
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()

    # create a function that will display the current score on screen
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    # create a function that will update the score based on the snake eating the food, 
    # clear the screen of the previous score, and update the scoreboard to show the new score
    def accumulate_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # create a function that will display "GAME OVER" in the center of the screen
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False,ALIGNMENT, FONT)
