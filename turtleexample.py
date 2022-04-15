'''
import turtle 


wn = turtle.Screen()
wn.bgcolor("lightblue")
myTurtle = turtle.Turtle() #naming turtle
myTurtle.color("white")
myTurtle.pensize(10)
myTurtle.penup()
myTurtle.left(90)
myTurtle.forward(80)
myTurtle.right(90)
myTurtle.forward(40)
myTurtle.pendown()
myTurtle.backward(80)
myTurtle.right(90)
myTurtle.forward(80)
myTurtle.left(90)
myTurtle.forward(80)
wn.mainloop() #assures that it stays open until manually close it 
'''

import turtle 

def drawSquare(t:turtle.Turtle):
    for i in range(4):
        t.forward(50)
        t.left(90)  #second two steps dont make sense 

def drawTriangle(t:turtle.Turtle):
    for i in range(3):
        t.forward(100)
        t.left(60)

wn = turtle.Screen()
wn.bgcolor("green")
myTurtle = turtle.Turtle()
myTurtle.color("red")
myTurtle.shape("blank")
myTurtle.pensize(3)
drawSquare(myTurtle) #bc its a function 
drawTriangle(myTurtle)
wn.exitonclick()