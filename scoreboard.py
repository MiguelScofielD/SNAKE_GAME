from turtle import Turtle

with open("data.txt",mode="r") as file:
    HIGH_SCORE = int(file.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,280)
        self.pencolor("white")
        self.hideturtle()
        self.high_score = HIGH_SCORE
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}",align="center", font=("Verdana",12, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def GameOver(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Verdana", 12, "normal"))