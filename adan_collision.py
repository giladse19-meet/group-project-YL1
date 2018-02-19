import time
import turtle
import time
import math
import random
from ball import Ball


BALLS = []
turtle.hideturtle()
MY_BALL = Ball(0,0,10,10,40,"green")
ball_1 = Ball(0,0,10,10,40,"green")
BALLS.append(ball_1)
MY_BALL.goto(50,50)
ball_1.goto(40,50)
MY_BALL.penup()
ball_1.penup()
turtle.penup()
def collide(ball_a,ball_b):
    #if ball_a.r == ball_b.r and ball_a.pos() == ball_b.pos():
        #return False
    d = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    if d  <= ball_a.r + ball_b.r:
    #if ball_a.pos == ball_b.pos:
        return True
        #print("truee")
    else:
        return False
        #print("false")
def check_color(ball_a,ball_b):
    if (ball_a.color()) == (ball_b.color()):
        return True
        
    else:
        return False
def collision_with_myball():
    for ball in BALLS:
        if collide(MY_BALL,ball)== True and check_color(MY_BALL,ball):
            ball.hideturtle()
            MY_BALL.hideturtle()
            print("trueeeee")


collide(ball_1,MY_BALL)
check_color(ball_1,MY_BALL)
collision_with_myball()
