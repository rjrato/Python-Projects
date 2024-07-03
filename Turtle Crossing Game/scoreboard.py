from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto((-180, 260))
        self.color("black")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Level {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
