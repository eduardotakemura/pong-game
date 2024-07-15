from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

## Setup the screen ##
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.tracer(0)

## Creating the paddles ##
left_coord = [(-350,-40),(-350,-20),(-350,0),(-350,20),(-350,40)]
right_coord = [(350,-40),(350,-20),(350,0),(350,20),(350,40)]
left_pad = Paddle(left_coord)
right_pad = Paddle(right_coord)

## Creating the ball ##
ball = Ball()
initial_speed = 0.1
ball_speed = initial_speed

## Setup the controls ##
screen.listen()
screen.onkey(fun=left_pad.move_up,key='w')
screen.onkey(fun=left_pad.move_down,key='s')
screen.onkey(fun=right_pad.move_up,key='Up')
screen.onkey(fun=right_pad.move_down,key='Down')

## Setting the scoreboard ##
scoreboard = Scoreboard()


game_on = True
while game_on:
    screen.update()
    time.sleep(ball_speed)
    ball.move()

    ## Checking hit with paddle ##
    if left_pad.check_hit(ball):
        ball.move()
        ball_speed *= 0.9
    elif right_pad.check_hit(ball):
        ball_speed *= 0.9
        ball.move()

    ## Checking a score point ##
    elif ball.xcor() > 400:
        ball.restart_game()
        left_pad.game_restart(left_coord)
        right_pad.game_restart(right_coord)
        scoreboard.left_score += 1
        scoreboard.restart_game()
        ball_speed = initial_speed

    elif ball.xcor() < -400:
        ball.restart_game()
        left_pad.game_restart(left_coord)
        right_pad.game_restart(right_coord)
        scoreboard.right_score += 1
        scoreboard.restart_game()
        ball_speed = initial_speed

    ## Checking hit with wall ##
    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.setheading(-ball.heading())
        ball.move()


screen.exitonclick()