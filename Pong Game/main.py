from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score, LEFT_POSITION, RIGHT_POSITION
import time

LEFT_PLAYER_STARTING_POSITION = (-350, 0)
RIGHT_COMPUTER_STARTING_POSITION = (350, 0)
TOP_WALL = 280
LOWER_WALL = -280

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_player_paddle = Paddle(LEFT_PLAYER_STARTING_POSITION)
left_player_score = Score(LEFT_POSITION)
right_player_paddle = Paddle(RIGHT_COMPUTER_STARTING_POSITION)
right_player_score = Score(RIGHT_POSITION)
ball = Ball()

screen.listen()
screen.onkeypress(right_player_paddle.up, key="Up")
screen.onkeypress(right_player_paddle.down, key="Down")
screen.onkeypress(left_player_paddle.up, key="w")
screen.onkeypress(left_player_paddle.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > TOP_WALL or ball.ycor() < LOWER_WALL:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(right_player_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_player_paddle) < 50
            and ball.xcor() < -320):
        ball.bounce_x()

    # Detect if the left player miss the ball
    if ball.xcor() > 400:
        left_player_score.increase_score()
        ball.reset_position()
        left_player_paddle.reset_position(LEFT_PLAYER_STARTING_POSITION)
        right_player_paddle.reset_position(RIGHT_COMPUTER_STARTING_POSITION)

    # Detect if right player miss the ball
    elif ball.xcor() < -400:
        right_player_score.increase_score()
        ball.reset_position()
        left_player_paddle.reset_position(LEFT_PLAYER_STARTING_POSITION)
        right_player_paddle.reset_position(RIGHT_COMPUTER_STARTING_POSITION)


screen.exitonclick()
