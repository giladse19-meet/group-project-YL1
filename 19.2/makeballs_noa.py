import turtle
from turtle import Turtle
import time
import random
import math

turtle.hideturtle()
turtle.tracer(delay=0)
turtle.setup(800,600)


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
for i in range(1):
    while(x<=380): 
      x=x+40
      color= (random.random(), random.random(), random.random())
      new = Ball(x,y,color)
      #turtle.update()
      Balls.append(new)
    y-=40
    x=-420


MY_BALL = Ball(0,0,"black")
MY_BALL.goto(0,-250)
MY_BALL.penup()
turtle.penup()

def collide(ball_a,ball_b):    
    d = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    print(ball_a.pos(),ball_b.pos())
    print(d)
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
        if collide(MY_BALL,ball):
          print("what am i doing with my life")
        if check_color(MY_BALL,ball):
          print("This is the worst group ever")
        if collide(MY_BALL,ball)== True:
            print("damn it")
            ball.hideturtle()
            MY_BALL.hideturtle()
            Balls.remove(ball)
            return True
        else:
          return False

#and check_color(MY_BALL,ball)== True:

def create_new_ball():
        global MY_BALL
        Balls.append(MY_BALL)
        MY_BALL = Ball(0, -250, "black")
        MY_BALL.pu()
        turtle.update()


def my_ball_move(angle):
    MY_BALL.left(angle)
    #while collision_with_myball==False:
      #MY_BALL.forward(10)


def angel(x, y):
    na = y / x
    an = math.atan(na)
    angle = math.degrees(an)
    MY_BALL.left(angle)
    
    while True:
      MY_BALL.fd(10)
      if collision_with_myball():
        break
      
    print(angle)

turtle.getscreen().onclick(angel)

def ball_on_field():
  if len(Balls)<1:
    return False
  else:
    return True

                        

#collision_with_myball()
#turtle.update()

#while ball_on_field == True:
        #create_new_ball()
        #collision_with_myball()
        #my_ball_move(angle)
        #turtle.update()
        
        
        
#while ball_on_field ==True:
 #       print("good job ")


