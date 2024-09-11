""" Snake Class """
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Snake class for snake game
    """

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Create a snake with 3 segments
        :return:
        """
        for _ in range(3):
            self.add_segment()
            self.segments[0].color("green")

    def add_segment(self):
        """
        Create a new segment for the snake
        :return:
        """
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment_after_eat(self):
        """
        Create a new segment for the snake
        :return:
        """
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def move_forward(self):
        """
        Move the snake forward
        :return:
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Move the snake up
        :return:
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Move the snake down
        :return:
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """
        Move the snake right
        :return:
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """
        Move the snake left
        :return:
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
