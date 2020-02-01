def evenOddEncrypt(plainText):
    evenStr=""
    oddStr=""
    index=0
    for ch in plainText:
        if index%2==0:
            evenStr+=ch
    else:
        oddStr+=ch
        index+=1
    return evenStr+oddStr
print(evenOddEncrypt("hello world"))


def evenOddDecrypt(cipherText):
#这里用整数除法，如果cipherText的长度是奇数，则halfLen*2比cipherText的长度少1
    halfLen=len(cipherText)//2
#oddStr的长度肯定是halfLen
    oddStrLen=halfLen
#evenStr的长度可能是halfLen，也可能是halfLen+1
    if(len(cipherText)%2==0):
        evenStrLen=halfLen
    else:
        evenStrLen = halfLen + 1


    evenStr = cipherText[:evenStrLen]
    oddStr = cipherText[evenStrLen:]
    str = ""
    for i in range(halfLen):
        str += evenStr[i]
        str += oddStr[i]
        if oddStrLen < evenStrLen:
            str += evenStr[-1]
    return str


s1 = evenOddEncrypt("hello world")
print(s1)
s2 = evenOddDecrypt(s1)
print(s2)