import turtle
import random
import math

myPen = turtle.Turtle()
def 算π(n):
    plot = turtle.getscreen()
    plot.setworldcoordinates(-2, -2, 2, 2)

    myPen.up()
    myPen.goto(-1,0)
    myPen.down()
    myPen.goto(1,0)
    myPen.up()
    myPen.goto(0,-1)
    myPen.down()
    myPen.goto(0,1)



    d=0
    for i in  range(0,n):
        x=random.random()
        y=random.random()
        myPen.up()
        myPen.goto(x, y)
        myPen.down()
        if math.sqrt(x**2+y**2)<1:
            d=d+1
            myPen.color("blue")
        else:
            myPen.color("red")
        myPen.dot()

    return d/n

print(算π(99999999)*4)
myPen.screen.mainloop()





#math.sqrt()
#random.random()