from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto((0, 260))
        self.color("white")
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

