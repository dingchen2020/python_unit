def myCount(list, item):
    count=0
    for i in list:
        if i==item:
            count+=1

    return count

list=["1",2,3,3,"xyz"]
print(myCount(list,"1"))


def myIn(list, item):
    for i in list:
        if i==item:
            return True
        else:
            return False

print(myIn(list,"2"))

def myReverse(list):
    newlist=[]
    for i in range(len(list)-1,0-1,-1):

        #for i2 in range(len(list)-1,0,-1):
        newlist.append(list[i])
        #i3=list[i]
        #newlist.insert(i2,i3)



    return newlist

print(myReverse(list))


def myIndex(list,item):
    count=0
    for i in list:
        if i==item:
            count += 1
    if count==0:
        return -1
    else:
        return count

print(myIndex(list,3))


def myInsert(list, index,item):
    newlist=[]
    for i in range(0,len(list),1):
        if i==index:

            newlist.append(item)
        else:
            newlist.append(list[i])

    return newlist


print( myInsert(list,3,5))

