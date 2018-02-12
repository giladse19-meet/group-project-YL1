import turtle
from turtle import Turtle
import time
import random
import math

turtle.setup(800,600)

class Ball(Turtle):
        def __init__(self,x,y,color):
                Turtle.__init__(self)
                self.x=x
                self.y=y
                self.penup()
                self.goto(x, y)
                self.r=20
                self.color(color,color)
                self.shape("circle")
                self.shapesize(2)

x=-400
y=250
Balls=[]

for i in range(3):
        while(x<=380):
                x=x+40
                color= (random.random(), random.random(), random.random())
                new = Ball(x,y,color)
                Balls.append(new)
        y-=40
        x=-400


        #limit the colors to red blue green !!!!!!!!!!!!!!!!!!!!!



