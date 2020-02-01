from u03_ex_03 import encrypt,解密

def removeChar(str: object, index: object):
    s1 =str[:index]
    s2 =str[index+1:]
    # print(s1)
    # print(s2)
    return s1 +s2


def removeDupChar(str):
    newStr =""
    for ch in str:
        if newStr.find(ch ) <0:
            newStr+=ch
    return newStr


def 生成密码(n):
    字母表 = "abcdefghijklmnopqrstuvwxyz "

    d= (removeDupChar(n))
    #字母表.find(q)
    dc = len(d)
    q = d[-1]
    qw=字母表.find(q)
    qw+=1
    qw2=字母表[qw]
    for i in range(0,dc):
        sd=d[i]
        字母表=removeChar(字母表,字母表.find(sd))

    qw3=字母表.find(qw2)


    z1=字母表[:qw3]
    z2=字母表[qw3:]

    return d+z2+z1


短语=input('请输入短语')
key=生成密码(短语)
print(key)
明文=input("请输入明文")
密文=(encrypt(明文,key))
短语=input('请输入短语')
key=生成密码(短语)
print(key)
明文=解密(密文,key)
print(明文)
print(密文)

