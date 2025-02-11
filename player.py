from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 300


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.setposition(STARTING_POSITION)
        self.shape('turtle')
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setposition(STARTING_POSITION[0], new_y)

    def finish(self):
        if self.distance(0, FINISH_LINE_Y) < 30:
            self.setposition(STARTING_POSITION)
            return True
