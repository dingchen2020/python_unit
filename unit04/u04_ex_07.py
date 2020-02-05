def myMean(list):
    平均数=0
    sum=0
    for i in range(0,len(list)):
        sum+=list[i]
    平均数=sum/len(list)
    return 平均数
myList=[1,2,3]
print(myMean(myList))
