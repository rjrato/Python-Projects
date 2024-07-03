import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Score()
cars = CarManager()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()

    # Detect collision with cars
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detect when turtle reach the finnish line
    if player.is_at_finnish_line():
        player.go_to_start()
        cars.level_up()
        score.increase_score()


screen.exitonclick()
