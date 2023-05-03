from turtle import Turtle

# Constants
ALIGNMENT = "center"
SCORE_FONT = ("Courier", 20, "bold")
GAMEOVER_FONT = ("Courier", 26, "bold")
SCORE_COLOR = "blue"
SCORE_COORDS = (0, 270)
START_SCORE = 0


class ScoreBoard(Turtle):

    def __init__(self):
        # Inheriting from Turtle Super-Class
        super().__init__()
        self.score = START_SCORE
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(SCORE_COORDS)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard by writing new score"""
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=SCORE_FONT)

    def game_over(self):
        """Triggers When Game is Over to print GameOver in centre"""
        self.goto(0, 0)
        self.write(f"G A M E  O V E R", align=ALIGNMENT,
                   font=GAMEOVER_FONT)

    def increase_score(self):
        """Increases score count by 1 at each call"""
        self.score += 1
        # clear the old written score, before writing new updated score
        self.clear()
        self.update_scoreboard()
