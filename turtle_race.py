from turtle import Turtle
from random import randint

akshay =Turtle()
akshay.color('black')
akshay.shape('turtle')
akshay.penup()
akshay.goto(-160,100)
akshay.pendown()

vasu =Turtle()
vasu.color('green')
vasu.shape('turtle')
vasu.penup()
vasu.goto(-160,70)
vasu.pendown()

ashu =Turtle()
ashu.color('blue')
ashu.shape('turtle')
ashu.penup()
ashu.goto(-160,40)
ashu.pendown()

lakshay =Turtle()
lakshay.color('red')
lakshay.shape('turtle')
lakshay.penup()
lakshay.goto(-160,10)
lakshay.pendown()

for movement in range(100):
    akshay.forward(randint(1,5))
    vasu.forward(randint(1,5))
    ashu.forward(randint(1,5))
    lakshay.forward(randint(1,5))



