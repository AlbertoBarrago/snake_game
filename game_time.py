""" Time play """
import time
from turtle import Turtle


class GameTimer(Turtle):
    """ Timer class for snake game """

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.start_time = time.time()
        self.is_game_active = True  # Track whether the game is active
        self.goto(0, -280)
        self.update_time()

    def update_time(self):
        """ Update the time to show in MM:SS format if the game is active """
        if self.is_game_active:
            self.clear()
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            time_str = f"{minutes:02}:{seconds:02}"  # Format time as MM:SS
            self.write(f"Time: {time_str}", align="center", font=("Arial", 14, "normal"))

            # Call update_time again after 1000ms (1 second) if the game is still active
            self.getscreen().ontimer(self.update_time, 1000)

    def reset_time(self):
        """ Reset the timer and restart it """
        self.start_time = time.time()
        self.is_game_active = True
        self.clear()
        self.update_time()

    def stop_timer(self):
        """ Stop the timer when the game ends """
        self.is_game_active = False
