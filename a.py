#키보드로 그림그리기
from turtle import *

def turn_right():
    setheading(0)
    forward(10)

def turn_left():
    setheading(180)
    forward(10)
def turn_up():
    setheading(90)
    forward(10)

def turn_down():
    setheading(270)
    forward(10)

def blak():
    clear()

shape("turtle")
speed(0)
onkeypress(turn_right(),"Right")
onkeypress(turn_up(),"Up")
onkeypress(turn_down(),"Down")
onkeypress(turn_left(),"Left")
onkeypress(blak(),"Escpace")
listen()
