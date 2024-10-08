""" Score module for snake game """
from numbers import Number
from turtle import Turtle

HIGH_SCORE = open("score.txt", mode="r").read()

class Score(Turtle):
    """
    Score class for snake game
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.high_score = int(HIGH_SCORE)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """
        Update the score
        :return:
        """
        self.write(f"Score: {self.score} - Highscore: {self.high_score}", align='center', font=('Arial', 18, 'normal'))

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
        if self.score > self.high_score:
            self.high_score = self.score
            open("score.txt", mode="w").write(str(self.score))
        self.clear()
        self.update_score()
