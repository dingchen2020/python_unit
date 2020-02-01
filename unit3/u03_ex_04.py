def removeChar(str, index):
    s1 = str[:index]
    s2 = str[index + 1:]
    return s1 + s2


def 生成密钥():
    import random
    字母表 = "abcdefghijklmnopqrstuvwxyz "
    密钥 = ""
    for i in range(1, 28):
        s = random.randint(0, len(字母表) - 1)
        # print(s)
        密钥 += 字母表[s]
        字母表 = removeChar(字母表, s)
    return 密钥


if __name__ == "__main__":
    print(生成密钥())
