def 频率统计(List):
    字典 = {}
    for i in List:
        if i in 字典:
            字典[i]+=1
        else:
            字典[i]=1
    print(字典)
    频率=[]
    keylist=list(字典.keys())
    print(keylist)
    valueslist=list(字典.values())
    print(valueslist)
    keylist.sort()

    for i in range(0,len(keylist)):
        print(keylist[i],":",字典[keylist[i]])
    for i in keylist:
        print(i, ":", 字典[i])

myList=[1, 3, 2, 3, 4, 3, 7, 8, 7, 9, 7, 10]
频率统计(myList)
