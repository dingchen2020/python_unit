count=0;
for i in range(2,101):
    for j in range(2,i//2+1):
        if(i%j==0):
            break
    else:
        print(i," is a prime number")
        count+=1

print("prime count is ",count)