def getsecond(data):
    return data[1]


def freqStat(dataList):
    分数=0
    tmpList=dataList[:]
    tmpList.sort()
    print("item"," ","freq")
    previous=tmpList[0] #previous记录上一个数据
    groupCount=0
    list=[]
    for current in tmpList: #current记录当前的数据
        if current[0]==previous[0]: #数据段没有切换
            groupCount+=1
            分数+=current[1]
        else: #数据段发生切换
            平均分=分数/groupCount
            list.append([previous[0],平均分]) #上一个数据的计数结束，输出
            previous=current #更新previous为新的数据
            groupCount=1 #统计从1开始
            分数=current[1]
    平均分 = 分数 / groupCount
    list.append([previous[0],平均分]) #输出最后一段数据
    list.sort(key=getsecond)
    print(list)
myList=[("alice",70),("bob",80),("joe",90),("bob",90),("alice",80),("joe",92),("alice",81)]

freqStat(myList)