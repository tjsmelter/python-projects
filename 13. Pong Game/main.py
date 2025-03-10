# The following code does not reflect original work, rather the result of learning via the course "100 Days of Code: The Complete Python Pro Bootcamp"

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)


# create the paddle objects and set them at the desired coordinates
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


# create the listen and onkey operations for moving the paddles up and down
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# create a while loop so that the game will continously operate 
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # create a conditional statement that accounts for if the ball bounces on the "north" and "south" borders and calls the bounce function if so
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # create a conditional statement that accounts for if the ball comes into contact with either of the paddles and call the bounce function if so
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if right paddles misses the ball, reset the ball and score one point for the left side
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # if the left paddle misses the ball, reset the ball and score one point for the right side
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
