""" Snake Game """
import time
from turtle import Screen
from food import Food
from score import Score
from snake import Snake

GAME_IS_ON = True
HEAD_DISTANCE = 20
LIMIT_WALL_DISTANCE = 290
SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(0)

snake = Snake()
food = Food()
score = Score()

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
    if snake.head.distance(food) < HEAD_DISTANCE:
        food.refresh()
        snake.add_segment_after_eat()
        score.increase_score()

    # Detect collision with wall
    if (snake.head.xcor() > LIMIT_WALL_DISTANCE or
            snake.head.xcor() < -LIMIT_WALL_DISTANCE or
            snake.head.ycor() > LIMIT_WALL_DISTANCE or
            snake.head.ycor() < -LIMIT_WALL_DISTANCE):
        GAME_IS_ON = False
        score.game_over()

SCREEN.exitonclick()
