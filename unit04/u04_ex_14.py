def getsecond(data):
    return data[1]


def freqStat(dataList):
    tmpList=dataList[:]
    tmpList.sort()
    print("item"," ","freq")
    previous=tmpList[0] #previous记录上一个数据
    groupCount=0
    list=[]
    for current in tmpList: #current记录当前的数据
        if current==previous: #数据段没有切换
            groupCount+=1
        else: #数据段发生切换
            list.append([previous,groupCount]) #上一个数据的计数结束，输出
            previous=current #更新previous为新的数据
            groupCount=1 #统计从1开始
    list.append([previous,groupCount]) #输出最后一段数据
    list.sort(key=getsecond)
    print(list)
myList=[1,3,2,3,4,3,7,8,7,9,7,10]
freqStat(myList)