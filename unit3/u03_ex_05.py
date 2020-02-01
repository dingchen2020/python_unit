from u03_ex_04 import 生成密钥
from u03_ex_03 import 密钥加密或解密,encrypt,解密
key=生成密钥()
print(key)
print(len(key))
m=encrypt("abcd ef",key)
print(m)
j=解密(m,key)
print(j)
