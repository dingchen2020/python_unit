def getMinMax(list):
    max=list[0]
    min=list[0]
    for i in range(1,len(list)):
        if list[i]>max:
            max=list[i]
        if list[i]<min:
            min=list[i]

    return max,min

list=[-9999,1,2,3,56,78,100]
print(getMinMax(list))