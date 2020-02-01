def 加密或解密(文章,n):
    字母表: str = "abcdefgjijklmnopqrstuvwxyz  "
    密文 = ""
    for i in range(0, len(文章)):
        位置 = 字母表.find(文章[i]) + n
        位置 = 位置 % 27

        密文 = 密文 + 字母表[位置]
    return 密文


def 加密(明文, n):

    return 加密或解密(明文, n)

def 解密(密文,n):
    return 加密或解密(密文, -n)

    return 明文


print(加密("abc",1))
print(解密("bcd",1))
