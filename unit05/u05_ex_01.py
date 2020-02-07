def getSecond(data):
    return data[1]

成绩单=open("socre01.txt","r")
字典={}
mylist=[]
for i in 成绩单:
    values = i.split()
    print(values[0], "got score:", values[1])
    字典[values[0]]=values[1]
print(字典)
Mylist=list(字典.items())
Mylist.sort(key=getSecond,reverse=True)
print(Mylist)
成绩单.close()

