from turtle import Turtle

COR = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DIS = 20

UP=90
RIGHT=0
LEFT=180
DOWN = 270

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for index in COR:
            self.add_segment()
    def add_segment(self):
            snake = Turtle('square')
            snake.color('white')
            snake.penup()
            snake.goto(COR[0])
            self.snakes.append(snake)

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.snakes[0].fd(MOVING_DIS)

    def up(self):
        if self.snakes[0].heading() !=DOWN:
            self.snakes[0].setheading(UP)

    def down(self):

        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)
