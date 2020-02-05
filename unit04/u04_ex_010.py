def 计算众数(list):
    字典 = {}
    value=0
    for i in list:
        if i in 字典:
            字典[i]+=1
        else:
            字典[i]=1

    最大值=max(字典.values())

    List=[]
    for i in 字典:
        if 字典[i]==最大值:
            List.append(i)
    return List
myList=[1, 3, 2, 3, 4, 3, 7, 8, 7, 9, 7, 10]
print(计算众数(myList))
