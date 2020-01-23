from turtle import Turtle,Screen


myPen=Turtle()
myPen2=Turtle()
myPen.color("red")
myPen2.color("blue")
myPen.up()
myPen2.up()

myPen2.goto(-300,0)
myPen.goto(300,0)

myPen.down()
myPen2.down()


for i in range(10,201,10):
    myPen.forward(i)
    myPen.right(90)
    myPen2.forward(i)
    myPen2.left(90)


myPen.screen.mainloop()