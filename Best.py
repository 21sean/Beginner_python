from turtle import *
from random import *
rectangleWidth = randint(300,600)
rectangleHeight = randint(300,600)
rectangle = randint(25,60)
def art(randomW, randomH):
    fillcolor(choice(('red','blue','pink',"gold","violet","cyan","white")))
    up()
    goto(250,-200)
    down()
    begin_fill()
    for i in range(2):
        left(90)
        forward(randomW)
        left(90)
        forward(randomH)
    end_fill()
speed(0)


def mondrian():
    for i in range(rectangle):
        art(randrange(150,rectangleWidth),randrange(150,rectangleHeight))

mondrian()

def leftEye():
    up()
    goto(-200,300)
    down()
    for i in range(256):
        forward(10)
        right(-275)
        circle(100)
def right_Eye():
    up()
    goto(200, 300)
    down()
    for i in range(256):
        forward(10)
        right(-275)
        circle(100)


def mouth():
    up()
    setheading(-27)
    goto(-225, -300)
    down()
    for i in range(500):
        forward(1)
        right(-.1)
        circle(50)




#mouth()
leftEye()
right_Eye()

done()