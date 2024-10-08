""" Score module for snake game """
from turtle import Turtle


class Score(Turtle):
    """
    Score class for snake game
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("score.txt", mode="r") as file:
            self.high_score = int(file.read())
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
