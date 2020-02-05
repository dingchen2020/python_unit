def getsecond(data):
    return data[1]


def freqStat(dataList):
    分数=0
    次数=0
    字典 = {}
    value = 0
    for i in dataList:
        name=i[0]
        score=i[1]
        if name in 字典:
            字典[name].append(score)
        else:
            字典[name] = [score]
    namelist=list(字典.keys())
    for i in namelist:
        scorelist=字典[i]
        平均数=sum(scorelist)/len(scorelist)
        print(i,平均数)

    print(字典)

myList=[("alice",70),("bob",80),("joe",90),("bob",90),("alice",80),("joe",92),("alice",81)]

freqStat(myList)