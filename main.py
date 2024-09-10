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
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        GAME_IS_ON = False
        print("Game Over")

screen.exitonclick()
