def n的平方根(n,s):
    x=1
    for i in  range(1,s+1):
        x=(x+n/x)/2
    return x

print(n的平方根(4,6))