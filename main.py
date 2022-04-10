#Need a score board class that is capable of traking p1 score and p2 score
#Need to create a turtle to draw a line down the center of the game
#Need a class to create the paddles on both side with Y axis movement only
#Need a class for the ball that start out moving in a random direction, can bounce off walls and paddles, and resets

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time
screen = Screen()
screen.setup(width=1400, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
#c_paddle = Paddle()
r_paddle = Paddle((625, 0))
l_paddle = Paddle((-625, 0))
ball = Ball()
scoreboard = Scoreboard()
game_on = True

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 610 or ball.distance(l_paddle) < 50 and ball.xcor() < -610:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 675:
        ball.reset_position()
        scoreboard.l_point()
        time.sleep(1)

    #Detect L paddle misses:
    if ball.xcor() < -675:
        ball.reset_position()
        scoreboard.r_point()
        time.sleep(1)














screen.exitonclick()