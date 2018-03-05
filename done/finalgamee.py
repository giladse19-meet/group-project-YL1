import turtle
from turtle import Turtle
import time
import random
import math
from threading import Thread



turtle.hideturtle()
turtle.tracer(delay=0)
turtle.setup(800,600)
turtle.bgcolor("black")

class Ball(Turtle):
        def __init__(self,x,y,color):
                Turtle.__init__(self)
                self.x=x
                self.y=y
                self.penup()
                self.goto(x, y)
                self.r=20
                self.color(color)
                self.shape("circle")
                self.shapesize(2)
                num=0
                num=random.randint(0,2)
                if num == 0:
                        self.color("red") 
                elif num==1:
                        self.color("green")
                elif num==2:
                        self.color("blue")

x=-420
y=250
Balls=[]
for i in range(3):
    while(x<=380): 
      x=x+40
      color= (random.random(), random.random(), random.random())
      new = Ball(x,y,color)
      Balls.append(new)
    y-=40
    x=-420


MY_BALL = Ball(0,0,"black")
MY_BALL.goto(0,-250)
MY_BALL.penup()
turtle.penup()

def collide(ball_a,ball_b):    
    d = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    if d  <= ball_a.r + ball_b.r:
        return True
        
    else:
        return False
        
        
def check_color(ball_a,ball_b):
    if (ball_a.color()) == (ball_b.color()):
        return True
        
    else:
        return False
def collision_with_myball():
    for ball in Balls:
        if collide(MY_BALL,ball) and check_color(MY_BALL,ball):
            ball.reset()
            Balls.remove(ball)
            ball.ht()
            MY_BALL.reset()
            MY_BALL.pu()
            MY_BALL.goto(-1000, -1000)
            MY_BALL.ht()
            return True
        elif collide(MY_BALL, ball):
            return True
    return False



def create_new_ball():
        global MY_BALL
        Balls.append(MY_BALL)
        MY_BALL = Ball(0, -250, "black")
        MY_BALL.pu()
        turtle.update()


def my_ball_move(angle):
    MY_BALL.forward(angle)
    print("Finished left")
    new_ball()

def angle(x, y):
    na = y / x
    an = math.atan(na)
    angle = math.degrees(an)
    
    if(angle < 0):
        angle = angle+ 180
    print(angle)
    MY_BALL.setheading(0)
    MY_BALL.left(angle)
    
    
    while True:
      MY_BALL.fd(10)
      if collision_with_myball():
        new_ball()
        break
        

def stop_game():
    for i in range(120):
        print(i)
        time.sleep(i)
    quit()

t1 = Thread(target = stop_game)
t1.start()

turtle.getscreen().onclick(angle)

def ball_on_field():
  if len(Balls)<1:
    return False
  else:
    return True

def new_ball():
        global MY_BALL
        Balls.append(MY_BALL)
        MY_BALL = Ball(0,0,"black")
        MY_BALL.goto(0,-250)
        MY_BALL.penup()

       
##
##while True :
##    if (MY_BALL.ycor()>600):
##        new_ball()

#collision_with_myball()
#turtle.update()

#while ball_on_field == True:
        #create_new_ball()
        #collision_with_myball()
        #my_ball_move(angle)
        #turtle.update()
        
        
        
#while ball_on_field ==True:
#       print("good job ")
