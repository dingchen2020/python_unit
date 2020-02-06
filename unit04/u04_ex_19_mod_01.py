import math
import statistics

def myStdDev(dataList):
    meanValue=statistics.mean(dataList)
    sum=0
    for data in dataList:
        sum+=(data-meanValue)**2
    return math.sqrt(sum/(len(dataList)-1))
