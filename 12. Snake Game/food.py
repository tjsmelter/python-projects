# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

from turtle import Turtle
import random


class Food(Turtle):
    # initialize a class for the "food" object, size, color, and random position on the screen
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize()
        self.color("purple")
        self.speed("fastest")
        random_x_cor = random.randint(-250, 250)
        random_y_cor = random.randint(-250, 250)
        self.penup()
        self.goto(random_x_cor, random_y_cor)
        self.generate_food()

    # create a function that will move the food object to a new random place on the screen
    def generate_food(self):
        new_food_x_cor = random.randint(-250, 250)
        new_food_y_cor = random.randint(-250, 250)
        self.penup()
        self.goto(new_food_x_cor, new_food_y_cor)
