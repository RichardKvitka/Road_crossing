from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-230,255)
        self.hideturtle()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=FONT)