from turtle import Turtle,Screen

def drawSquare(myTurtle,sideLength):
    myTurtle.forward(sideLength)
    myTurtle.left(90)
    myTurtle.forward(sideLength)
    myTurtle.left(90)
    myTurtle.forward(sideLength)
    myTurtle.left(90)
    myTurtle.forward(sideLength)
    myTurtle.left(90)





myPen=Turtle()
myPen.color("red")
myPen.fillcolor("blue")
drawSquare(myPen,20)
drawSquare(myPen,50)
myPen.screen.mainloop()