from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_segment(position)

    def add_snake_segment(self, position):
        new_line_segment = Turtle(shape="square")
        new_line_segment.color("white")
        new_line_segment.penup()
        new_line_segment.goto(position)
        self.segments.append(new_line_segment)

    def extend_snake(self):
        self.add_snake_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[seg - 1].xcor()
            next_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(next_x, next_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def turn_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def turn_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def turn_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
