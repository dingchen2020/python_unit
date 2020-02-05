def getmin(list):
    maxValue=list[0]
    for i in range(1,len(list)):
        if list[i]<maxValue:
            maxValue=list[i]
    return maxValue

def getMax(list):
    maxValue=list[0]
    for i in range(1,len(list)):
        if list[i]>maxValue:
            maxValue=list[i]
    return maxValue







def getmin2(list):
    maxValue=list[0]
    for value in list[1:]:
        if value<maxValue:
            maxValue=value
        return maxValue

def getRange(list):
    return getMax(list)-getmin(list)




list=[2,3,3,12]
print(getmin(list))
print(getmin2(list))
print(getRange(list))

