with open('word','r') as word:
    line=[]
    conunt2=0
    字典={}
    for i in word:
        conunt2+=1
        for i2 in i.split():
            if i2 in 字典:
                lineList=字典[i2]
                if (conunt2 not in lineList):
                    字典[i2].append(conunt2)
            else:
                字典[i2] = [conunt2]
    print(字典)

    with open('word2','w') as word2:
        keylist=list(字典.keys())
        keylist.sort()
        for i3 in keylist:
            value=字典[i3]

            word2.write(i3)
            word2.write(':')
            for i4 in value:
                word2.write(str(i4)+' ')

            word2.write('\n')