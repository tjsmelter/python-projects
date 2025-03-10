# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

from turtle import Turtle

class Ball(Turtle):

    # initialize the ball, with color, shape and speed
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .1

    # create a function that takes the current coordinates of the ball and moves it by 10 units each way
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    # create a function that sends the ball in the opposite direction after coming in contact with the wall or paddle
    def bounce_y(self):
        self.y_move *= -1

    # same as above but for x
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .9

    # create a function that resets the ball position to the center and moves it in the opposite direction from where it was going last
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = .1
        self.bounce_x()
