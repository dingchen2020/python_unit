def 列表排序(x):
    数字数=0
    for i in x:
        if i >="0" and i<="9":
            数字数+=1

    return 数字数




list=["1bc","1sd23","3f4e"]
list.sort(key=列表排序)
print(list)

