

def 中位数(list):

    copyList=list[:] #使用slice方法生成新的list
    copyList.sort()
    余数=len(copyList)%2
    listLen=len(copyList)
    if 余数==1:
        return (copyList[listLen//2])
    if 余数==0:
        z1=copyList[listLen//2-1]
        z2=copyList[listLen//2]
        return ((z1+z2)/2)

list=[1,2,4,3,5]
print(中位数(list))