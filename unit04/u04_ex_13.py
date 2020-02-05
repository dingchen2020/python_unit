studentNames=["james","peter","rose","sue"]
scores=[85,90,91,78,99]

def getSecond(data):
    return data[1]

def getNameLen(data):
    return len(data[0])
def getnamesecond(data):
     return data[0][1]
     
def 制作字典(value,key):
    字典={}
    for i in range(0,len(key)):
        字典[key[i]]=value[i]

    return 字典
mydict=(制作字典(scores,studentNames))
Mylist=list(mydict.items())
Mylist.sort(key=getSecond,reverse=True)
Mylist.sort(key=getNameLen)
Mylist.sort(key=getnamesecond)

print(Mylist)
