import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

player = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")
screen.onkey(player.go_left, "a")
screen.onkey(player.go_right, "d")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.07)
    player.move()

    # Detect collision with food
    if player.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        player.extend()

    # Detect collision with wall
    if player.head.xcor() > 290 or player.head.xcor() < -290 or player.head.ycor() > 290 or player.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in player.segments[1:]:
        if player.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()