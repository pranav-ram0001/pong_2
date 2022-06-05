from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.speed = 1

    def move(self):
        new_x = self.xcor() + (self.x_move * self.speed)
        new_y = self.ycor() + (self.y_move * self.speed)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed += 0.1

    def restart(self):
        self.goto(0, 0)
        self.speed = 1
        self.x_move *= -1
        self.y_move *= -1
