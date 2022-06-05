from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 35, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.text = ""

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
            return net
        self.net = create_net()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("Courier", 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=("Courier", 80, 'normal'))

    def game_over(self):
        self.clear()
        self.net.clear()
        self.goto(0, 0)
        if self.r_score > self.l_score:
            self.text = "The player on the right won!"
        else:
            self.text = "The player on the left won!"

        self.write(self.text, align=ALIGNMENT, font=FONT)

    def exit_game(self):
        self.goto(0, 0)
        self.clear()
        self.net.clear()
        self.write("Game over", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1
