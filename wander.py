from turtle import *
from random import randint

speed(5)
shape('turtle')

def wander():
    while True:
        fd(3)
        if xcor() >= 300 or xcor() <= -300 or ycor() <= -300 or ycor() >= 300:
            lt(randint(90,180))

wander()