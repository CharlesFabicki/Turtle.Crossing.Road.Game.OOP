import time
from turtle import Screen
from player import Player
from cars import Cars
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Game. Use ↑ key to move the turtle upwards")
screen.tracer(0)

player = Player()
cars = Cars()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 23:
            game_is_on = False
            score.game_over()

    if player.player_finish():
        player.start_line()
        cars.next_level()
        score.increase_level()

screen.exitonclick()