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

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left,"Left")
screen.onkey(snake.turn_right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Collision with food
    if snake.snake_head.distance(food) < 25:
        food.generate_food()
        scoreboard.accumulate_score()
        snake.extend_snake()

    #Crash into wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.ycor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Crash into tail
    #if snake head crashed into any segment in the tail: then game over
    for segment in snake.segments[1:]:
        # if segment == snake.snake_head:
        #     pass
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
