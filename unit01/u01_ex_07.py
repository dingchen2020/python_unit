from turtle import Turtle,Screen

def drawSquare(myTurtle,sideLength):
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.left(90)

myPen=Turtle()
myPen.color("red")

#n=10

for i in range(10,101,10):
    drawSquare(myPen,i)
    myPen.up()
    x,y=myPen.position()
    myPen.goto(x-5,y-5)
    myPen.down()

myPen.up()
x,y=myPen.position()
myPen.goto(x+5,y+5)
myPen.screen.mainloop()