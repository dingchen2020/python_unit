from turtle import Turtle,Screen

myPen=Turtle()
myPen.color("red")
for i in range(10,501,10):
    myPen.forward(i)
    myPen.right(90)

myPen.screen.mainloop()