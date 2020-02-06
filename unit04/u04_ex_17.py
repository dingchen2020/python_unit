

from turtle import Turtle
myPen = Turtle()
def freqHistogram(dataList):
    countDict={}
    for data in dataList:
        if data in countDict:
            countDict[data]+=1
        else:
            countDict[data]=1
    return countDict


def 画长方形():
    xList = list(dict.keys())
    for i in range(len(xList)):
        myPen.goto(i + 1, -0.2)
        myPen.write(str(xList[i]))  # 写数字
        myPen.goto(i + 1, 0)
        myPen.down()
        myPen.goto(i + 1, dict[xList[i]])  # 画线
        myPen.goto(i+1.3,dict[xList[i]])
        myPen.goto(i+1.3,0)

def draw(dict):


    xList = list(dict.keys())
    maxX = len(xList)
    print(maxX)
    yList = list(dict.values())
    maxY = max(yList)
    xList.sort()
    myPen = Turtle()
    win = myPen.getscreen()
    win.setworldcoordinates(-1, -1, maxX + 1, maxY + 1)  # 设定坐标系大小
    myPen.hideturtle()  # 隐藏光标形状
    #画X轴
    myPen.up()
    myPen.goto(0,0)
    myPen.down()
    myPen.goto(maxX,0)
    myPen.up()
    myPen.goto(0, 0)
    myPen.down()
    myPen.goto(0,maxY)
    #画Y轴和最大，最小两个数值
    myPen.up()
    myPen.goto(-0.1,0)
    myPen.write("0")
    myPen.goto(-0.1, maxY)
    myPen.write(str(maxY))
    xList = list(dict.keys())
    for i in range(len(xList)):
        myPen.goto(i + 1.15, -0.2)
        myPen.write(str(xList[i]))  # 写数字
        myPen.goto(i + 1, 0)
        myPen.down()
        myPen.begin_fill()
        myPen.goto(i + 1, dict[xList[i]])  # 画线
        myPen.goto(i + 1.3, dict[xList[i]])
        myPen.goto(i + 1.3, 0)
        myPen.end_fill()
        myPen.up()

    win.mainloop()
myList=[1,3,2,3,4,3,7,8,7,9,7,10,7,2,1,5]
freqHistogram(myList)
draw(freqHistogram(myList))
