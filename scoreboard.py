from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as high_score:
            self.high_score = high_score.read()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.speed("fastest")
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(str(self.high_score))

        self.score = 0
        self.refresh_score()
