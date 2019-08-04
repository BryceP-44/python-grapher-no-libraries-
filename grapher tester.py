from turtle import *
import math

#use the scale only when you mess with non-linear functions
#just multiply it in the fron of the function
screen_width = 1920

#however many integers of x you want
#such as the graph loking like it goes to x of 10...(10,y)
clicks = 10

scale = 1/((screen_width/clicks)*.5)
width = 200     #how far the turtles should go left and right
x1 = 0
y1 = 0
x2 = 0
y2=0
#make another turtle
t2=Turtle()

for i in range(abs(width)*2):
    #first turtle
    #put the function here
    y1= 50*math.sin(x1* .1)
    goto(x1, y1)
    x1=x1+1

    #second turtle going backwards
    #put the function here
    y2=50 * math.sin(x2*.1)
    t2.goto(x2, y2)
    x2=x2-1