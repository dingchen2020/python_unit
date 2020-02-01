alphabet="abcdefghijklmnopqrstuvwxyz "
def encrypt(plainText,key):
    str=""
    for ch in plainText:
        index=alphabet.find(ch)
        #print(index)
        if index<0:
            print("unsupport char:",ch)
            return ""
        ch2=key[index]
        str+=ch2
    return str
myPlain="hello world"
myKey=" bpzhgocvjdqswkimlutneryaxf"
myCipher=encrypt(myPlain,myKey)
print("encrypt=",myCipher)


def 解密(m,key):
    mc=len(m)
    j = ""
    for i in range(0,mc):
        j1=key.find(m[i])
        j2=alphabet[j1]
        j+=j2

    return j

print(解密("chqqkfrklqz"," bpzhgocvjdqswkimlutneryaxf"))


