from turtle import Turtle,Screen

def drawSquare(myTurtle,sideLength):
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.left(90)


myPen=Turtle()
myPen.color("red")

for i in range(10,101,10):
    drawSquare(myPen,i)
myPen.screen.mainloop()