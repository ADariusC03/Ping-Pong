# Simple Pong Game
# By A'Darius Craig Nov.9, 2020
# Game Keys: Left side { w-Up, s-Down } , Right side { i-Up, k-Down}

# See Who Can Score The Most And Have Bragging Rights!!

import turtle
import os

wn = turtle.Screen()
wn.title("Ping Pong @A'DariusC03")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A -> Left side
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation for the turtle module
paddle_a.shape("square")
paddle_a.color("Green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Default its 20px wide by 20px high
paddle_a.penup() # Doesn't draw a line
paddle_a.goto(-350, 0) # -350=x, 0=y... negative 350 for left side

# Paddle B -> Right side
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of animation for the turtle module
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # Default its 20px wide by 20px high
paddle_b.penup() # Doesn't draw a line
paddle_b.goto(350, 0) # -350=x, 0=y... positve 350 for right side

# Ball -> Center
ball = turtle.Turtle()
ball.speed(0) # speed of animation for the turtle module
ball.shape("square")
ball.color("white")
ball.penup() # Doesn't draw a line
ball.goto(0, 0) # 0=x, 0=y .. starts in the middle
ball.dx = 2 # d = delta change/ x speed - move diagonal
ball.dy = -2 # everytime the ball moves it moves by 2px - move up to down

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Host A: 0   Host B: 0 ", align="center", font=("Droid Sans Mono", 20, "normal"))

# Score
score_a = 0
score_b = 0



# Making Function
def paddle_a_up():
    y = paddle_a.ycor() # y cordinates to go up and down by 20px
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() # y cordinates to go up and down by 20px
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # y cordinates to go up and down by 20px
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # y cordinates to go up and down by 20px
    y -= 20
    paddle_b.sety(y)



# Keyboard binding
wn.listen() # Listens for keyboard input
wn.onkeypress(paddle_a_up, "w") # Lside - when the user press a the function goes up
wn.onkeypress(paddle_a_down, "s") # Lside - Down function
wn.onkeypress(paddle_b_up, "i") # Rside - up function
wn.onkeypress(paddle_b_down, "k") # Rside - down fucntion




# Main Game Loop Function
while True:
    wn.update()


    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:   # Direction of the ball
        ball.sety(290)
        ball.dy *= -1       # Make the direction reverse
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Host A: {}   Host B: {} ".format(score_a, score_b), align="center", font=("Droid Sans Mono", 20, "normal"))
        

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Host A: {}   Host B: {} ".format(score_a, score_b), align="center", font=("Droid Sans Mono", 20, "normal"))

    # Paddle & Ball collisons
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")