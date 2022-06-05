from turtle import Turtle


def create_net():
    net = Turtle()
    net.hideturtle()
    net.color('white')
    net.penup()
    net.goto(0, 300)
    net.setheading(270)
    for i in range(30):
        net.pendown()
        net.forward(10)
        net.penup()
        net.forward(10)
