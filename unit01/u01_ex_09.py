from turtle import Turtle,Screen
import math
myPen=Turtle()


def drawcircie (r,n):
    side=2*r*math.sin(math.radians(180/n))
    jiao=360/n
    for i in range(n):
        myPen.forward(side)
        myPen.left(jiao)

drawcircie (100,9)
myPen.screen.mainloop()