# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

from turtle import Turtle

class Paddle(Turtle):
    # initialize the paddle object for shape, color and to go to a given position as indicated in an argument
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # create a function that will gather the current y coordinate and move the paddle "north" 20 units 
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # create a function that will gather the current y coordinate and move the paddle "south" 20 units 
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
