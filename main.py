from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import keyboard
import time

STARTING_X_COR_R = 350
STARTING_X_COR_L = -350
game_is_on = False

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
SCREEN_HEIGHT = screen.canvheight
SCREEN_WIDTH = screen.canvwidth

game_length = int(screen.textinput(title="Duration of the game", prompt="Until how many points will you play? "))

r_paddle = Paddle(STARTING_X_COR_R)
l_paddle = Paddle(STARTING_X_COR_L)
ball = Ball()
scoreboard = Score()

screen.listen()

screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')

screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')


if game_length:
    game_is_on = True

while game_is_on:
    time.sleep(0.05)
    scoreboard.update_scoreboard()
    screen.update()
    ball.move()

    # detect ball collision with wall
    if ball.ycor() > SCREEN_HEIGHT - 20 or ball.ycor() < -SCREEN_HEIGHT + 20:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > SCREEN_WIDTH - 80 or ball.distance(
            l_paddle) < 50 and ball.xcor() < -SCREEN_WIDTH + 80:
        ball.bounce_x()

    if ball.xcor() > SCREEN_WIDTH - 20:
        ball.restart()
        scoreboard.l_point()

    if ball.xcor() < -SCREEN_WIDTH + 20:
        ball.restart()
        scoreboard.r_point()
    if scoreboard.l_score >= game_length or scoreboard.r_score >= game_length:
        ball.reset()
        r_paddle.reset()
        l_paddle.reset()
        scoreboard.game_over()
        game_is_on = False

    if keyboard.is_pressed("Escape"):
        ball.reset()
        r_paddle.reset()
        l_paddle.reset()
        scoreboard.exit_game()
        game_is_on = False


screen.update()
screen.exitonclick()
