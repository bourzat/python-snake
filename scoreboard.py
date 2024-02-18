from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 24, 'normal')
FILE = "data.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open(FILE, mode='r') as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open(FILE, mode="w") as file:
                file.write(str(self.high_score))
                self.score = 0
                self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
