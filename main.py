from turtle import Screen
import time
from food import Food
from snake import Snake
from  scoreboard import Scoreboard


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Snake Game')

timmy = Snake()
food = Food()
scores = Scoreboard()
screen.listen()
screen.onkey(timmy.up, "Up")
screen.onkey(timmy.down, "Down")
screen.onkey(timmy.left, "Left")
screen.onkey(timmy.right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    timmy.move()
    if timmy.snakes[0].distance(food) < 17:
        food.refresh()
        scores.increase_score()
        timmy.add_segment()

    if timmy.snakes[0].xcor()>280 or timmy.snakes[0].xcor()<-280 or timmy.snakes[0].ycor()>280 or timmy.snakes[0].ycor()<-280 :
        scores.game_over()
        is_game_on = False
    for segment in timmy.snakes[1:]:
            if timmy.snakes[0].distance(segment)<10:
                scores.game_over()
                is_game_on = False


screen.exitonclick()