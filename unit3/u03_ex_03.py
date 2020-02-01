
def 密钥加密或解密(w,n,n2):
    mc = len(w)
    j = ""
    for i in range(0, mc):

        j1 = n.find(w[i])
        j2 = n2[j1]
        j += j2

    return j


def encrypt(p,k):
    return 密钥加密或解密(p,"abcdefghijklmnopqrstuvwxyz ",k)


def 解密(m,key):
   return 密钥加密或解密(m,key,"abcdefghijklmnopqrstuvwxyz ")

if __name__=="__main__":
    print(encrypt("hello world"," bpzhgocvjdqswkimlutneryaxf"))
    print(解密("chqqkfrklqz"," bpzhgocvjdqswkimlutneryaxf"))