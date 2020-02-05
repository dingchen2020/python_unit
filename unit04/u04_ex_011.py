def 计算众数(list):
    众数=[]
    MyList=[0]*max(list)
    for i in list:
        MyList[i-1]+=1
    print(MyList)
    最大值 = max(MyList)
    for i in range(0,len(MyList)):
        if MyList[i]==最大值:
            众数.append(i+1)
    return 众数
list=[1,2,2,3,4,4,4,5,5,5]
print(计算众数(list))