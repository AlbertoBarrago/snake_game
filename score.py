""" Score module for snake game """
from turtle import Turtle


class Score(Turtle):
    """
    Score class for snake game
    """

    def __init__(self):
        super().__init__()
        self.write('Score', align='center', font=('Arial', 18, 'normal'))
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """
        Update the score
        :return:
        """
        self.write(f"Score: {self.score}", align='center', font=('Arial', 18, 'normal'))

    def game_over(self):
        """
        Game over
        :return:
        """
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 18, 'normal'))

    def increase_score(self):
        """
        Increase the score
        :return:
        """
        self.score += 1
        self.clear()
        self.update_score()
