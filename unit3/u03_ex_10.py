def getKeyChar(key,charInPlainIndex):
    keyLen=len(key)
    return key[charInPlainIndex%keyLen]



字母表="abcdefghijklmnopqrstuvwxyz "
def 加密(明文, key):
    spaceCount=0
    密文 = ""
    for i in  range(0,len(明文)):
        if 明文[i]==" ":
            #密文+=" "
            spaceCount+=1
        else:
            c=getKeyChar(key,i-spaceCount)
            #print(i)
            #print(key)
            s1=字母表.find(c)
            s2=字母表.find(明文[i])
            s3=s1+s2
            s4=s3%26
            #print(s4)
            密文+=字母表[s4]

    return 密文






def 解密(密文,key):
    明文=""
    for i in range(0,len(密文)):

            c=getKeyChar(key, i)

            s1=字母表.find(c)

            s2=字母表.find(密文[i])

            s3=s2-s1
            s4=s3 % 26

            明文+=字母表[s4]

    return 明文
s=加密("caa aaa","bcdef")
print(s)
s2=解密(s,"bcdef")
print(s2)