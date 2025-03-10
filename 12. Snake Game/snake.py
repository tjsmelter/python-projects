# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # initialize the class of snake to have a list of segments, the "create snake" method and the "snake head" attribute as the first segment in the segments list
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    # create a function that creates an initial snake of three blocks using the three coordinates from STARTING_POSITIONS
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_segment(position)

    # create a function that creates a new snake segment adds it to the segments list and takes in an argument that accounts for the current position of the snake
    def add_snake_segment(self, position):
        new_line_segment = Turtle(shape="square")
        new_line_segment.color("white")
        new_line_segment.penup()
        new_line_segment.goto(position)
        self.segments.append(new_line_segment)

    # create a function that finds the current position of the of the snake and adds the new block to the last element in the list
    def extend_snake(self):
        self.add_snake_segment(self.segments[-1].position())

    # create a function that connects the blocks to move as all one object
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[seg - 1].xcor()
            next_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(next_x, next_y)
        self.snake_head.forward(MOVE_DISTANCE)

    # create a function that moves the snake "north" on the screen
    def turn_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    # create a function that moves the snake "south" on the screen
    def turn_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    # create a function that moves the snake "east" on the screen
    def turn_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    # create a function that moves the snake "west" on the screen
    def turn_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
