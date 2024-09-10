""" Snake Game """
import time
from turtle import Screen
from snake import Snake
from food import Food

GAME_IS_ON = True
SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(0)

snake = Snake()
food = Food()

while GAME_IS_ON:
    SCREEN.update()
    time.sleep(0.1)
    snake.move_forward()
    SCREEN.listen()
    SCREEN.onkey(snake.up, "Up")
    SCREEN.onkey(snake.down, "Down")
    SCREEN.onkey(snake.right, "Right")
    SCREEN.onkey(snake.left, "Left")

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_segment_after_eat()
        print("nom nom nom")

    # Detect collision with wall
    if (snake.head.xcor() > 280 or
            snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or
            snake.head.ycor() < -280):
        GAME_IS_ON = False
        print("Game Over")

SCREEN.exitonclick()
