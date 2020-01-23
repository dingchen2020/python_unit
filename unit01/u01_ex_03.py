
import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False

    return True

for i in range(2,101):
    if isPrime(i):
        print(i)