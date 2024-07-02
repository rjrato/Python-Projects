from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 80, "normal")
LEFT_POSITION = (-100, 200)
RIGHT_POSITION = (100, 200)


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.goto(position)
        self.color("white")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
