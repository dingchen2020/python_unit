

from turtle import Turtle

def freqHistogram(dataList):
    countDict={}
    for data in dataList:
        if data in countDict:
            countDict[data]+=1
        else:
            countDict[data]=1
    return countDict



def draw(dict,myPen,mean,stddev):


    xList = list(dict.keys())
    maxX = max(xList)
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
    xList.sort()
    for i in range(1,xList[-1]+1):
        myPen.goto(i + 0.15, -0.2)
        myPen.write(str(i))  # 写数字
        myPen.goto(i, 0)
        myPen.down()
        if i in dict:
            myPen.begin_fill()
            myPen.goto(i, dict[i])  # 画线
            myPen.goto(i+0.3, dict[i])
            myPen.goto(i+0.3, 0)
            myPen.end_fill()
        myPen.up()
    myPen.color('red')
    myPen.goto(mean,0)
    myPen.down()
    myPen.goto(mean,maxY)
    myPen.up()
    myPen.color('blue')
    myPen.goto(mean-stddev, 0)
    myPen.down()
    myPen.goto(mean-stddev, maxY)
    myPen.up()
    myPen.goto(mean+stddev, 0)
    myPen.down()
    myPen.goto(mean+stddev, maxY)
    myPen.up()
    win.mainloop()

if __name__ == "__main__":
    myList=[1,3,2,3,4,3,7,8,7,9,7,10,7,2,1,5]
    myPen = Turtle()
    myDict=freqHistogram(myList)
    draw(myDict,myPen)
