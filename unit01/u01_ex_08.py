from turtle import Turtle,Screen

def Y值(x):
    y=(x / 100) ** 2 * 100
    return y
myPen=Turtle()
myPen.up()
myPen.goto(-500,0)
myPen.down()
myPen.color("blue")
myPen.goto(500,0)
myPen.up()
myPen.goto(0,500)
myPen.down()
myPen.goto(0,-500)

myPen.up()
myPen.goto(-500,Y值(-500))
myPen.down()
for x in range(-500,501,1):
    myPen.goto(x,Y值(x))
myPen.screen.mainloop()