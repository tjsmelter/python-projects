from turtle import Turtle
import random

class Food(Turtle):
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
    
    def generate_food(self):
        new_food_x_cor = random.randint(-250, 250)
        new_food_y_cor = random.randint(-250, 250)
        self.penup()
        self.goto(new_food_x_cor, new_food_y_cor)
