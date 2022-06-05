from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_coordinate):
        super().__init__()
        self.shape('square')
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(x_coordinate, 0)


    def up(self):
        if not self.ycor() > 220:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if not self.ycor() < -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
