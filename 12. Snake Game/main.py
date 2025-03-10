# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# create the onkey and listen commands to allow the user to control the snake
screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left,"Left")
screen.onkey(snake.turn_right, "Right")


# create a while loop so that the game will continuously run until the snake hits the border or itself
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # create a conditional statement that accounts for a collision with food on screen
    if snake.snake_head.distance(food) < 25:
        food.generate_food()
        scoreboard.accumulate_score()
        snake.extend_snake()

    # create a conditional statement that acconts for a collision with the wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.ycor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # create a conditional statement that accounts for a collision with its tail
    #if snake head crashed into any segment in the tail: then game over
    for segment in snake.segments[1:]:
        # if segment == snake.snake_head:
        #     pass
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
