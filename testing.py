from turtle import Turtle, Screen
import time

screen = Screen()

tim = Turtle()
screen.listen()

heading = tim.heading()

def up():
    tim.setheading(0)
    tim.setheading(90)

def down():
    tim.setheading(0)
    tim.setheading(270)

def right():
    tim.setheading(0)
    tim.setheading(0)
def left():
    tim.setheading(0)
    tim.setheading(180)

screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")


screen.exitonclick()
