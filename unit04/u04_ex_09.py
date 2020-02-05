'''myDict={"james":3,"peter":2,"rose":5}
print(myDict["james"])
myDict["james"]+=1
print(myDict["james"])
print(myDict.keys()) #dict_keys(['james', 'peter', 'rose'])
print(myDict.values()) #dict_values([4, 2, 5])
print(myDict.items()) #dict_items([('james', 4), ('peter', 2), ('rose', 5)])'''
studentNames=["james","peter","rose","sue"]
scores=[85,90,91,78,99]

def 制作字典(value,key):
    字典={}
    for i in range(0,len(key)):
        字典[key[i]]=value[i]

    return 字典

字典=制作字典(scores,studentNames)
print(字典)
字典["peter"]+=5
key=list(字典.values())
key.sort()
print(key)
平均成绩=sum(key)/len(key)
print(平均成绩)
字典["rose"]=85
字典.pop('sue')
print(字典)


def getScore(name):
    print(name in 字典)
    if name in 字典:

        return 字典[name]
    else:
        return -1

print(getScore('peter'))




def 打印成绩单():
    字典=(制作字典(scores, studentNames))
    nameList=list(字典.keys())
    nameList.sort()
    for name in nameList:
        print(name,字典[name])

打印成绩单()