from u04_ex_19_mod_01 import myStdDev
import statistics
from u04_ex_19_mod_02 import freqHistogram,draw
import random
from turtle import Turtle

myList=[]
for i in range(1000):

    myList.append(int(random.gauss(25,10)))
print(myList)
平均值=statistics.mean(myList)
方差=myStdDev(myList)
myPen = Turtle()
myDict=freqHistogram(myList)
draw(myDict,myPen,平均值,方差)
print(平均值)
print(方差)
