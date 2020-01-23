from turtle import Turtle,Screen

def  drawRectangle(myTurtle,reccWidth,recHeight):
    myTurtle.forward(reccWidth)
    myTurtle.left(90)
    myTurtle.forward(recHeight)
    myTurtle.left(90)
    myTurtle.forward(reccWidth)
    myTurtle.left(90)
    myTurtle.forward(recHeight)
    myTurtle.left(90)





myPen=Turtle()
myPen.color("red")
myPen.fillcolor("blue")
drawRectangle(myPen,20,60)
drawRectangle(myPen,50,100)
myPen.screen.mainloop()