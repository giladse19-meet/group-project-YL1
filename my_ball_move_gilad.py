import turtle
import math

def my_ball_move(angel):
    turtle.left(angel)


def angel(x, y):
    na = y / x
    an = math.atan(na)
    a = math.degrees(an)
    turtle.left(a)
    turtle.fd(50)
    print(a)
    return(a)

##screen width, screen_hieght,event
##screen width, screen_hieght,balls,
##while collision == True:
##my_ball.forward(10)

turtle.getscreen().onclick(angel)
#my_ball_move(angel())
