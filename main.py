""" Snake Game """
import time
from turtle import Screen
from snake import Snake

GAME_IS_ON = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()


while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)

    snake.move_forward()

screen.listen()
screen.exitonclick()
