def getKeyChar(key,charInPlainIndex):
    keyLen=len(key)
    return key[charInPlainIndex%keyLen]



字母表="abcdefghijklmnopqrstuvwxyz "
def 加密(明文, key):

    密文 = ""
    for i in  range(0,len(明文)):
        if 明文[i]==" ":
            密文+=" "
        else:
            c=getKeyChar(key,i)
            #print(i)
            #print(key)
            s1=字母表.find(c)
            s2=字母表.find(明文[i])
            s3=s1+s2
            s4=s3%26
            #print(s4)
            密文+=字母表[s4]

    return 密文


print(加密("caa aaa","bcdef"))



def 解密(密文,key):
    明文=""
    for i in range(0,len(密文)):
        if 密文[i] ==" ":
            明文 += " "
        else:
            c=getKeyChar(key, i)
            #print(i)
            #print(key)
            s1=字母表.find(c)
            #print(s1)
            s2=字母表.find(密文[i])
            #print(s2)
            s3=s2-s1
            s4=s3 % 26
            #print(s4)
            明文+=字母表[s4]

    return 明文


print(解密("dcd fbc","bcdef"))