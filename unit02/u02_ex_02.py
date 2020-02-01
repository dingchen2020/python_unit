import math

def π(n):
    sum=0
    for i in range(1,n+n-1,4):
        sum+= 1 / i - 1 / (i+2)

    #for i2 in range(3,n*3*n,4):
        #f2=i2

    #for π2 in range(1,n+n2+1,1/f-1/f2,):
        #f3=π2
    return sum



print(π(999999)*4)

#sum=0
#for i in range(1,101):
    #sum=sum+i
