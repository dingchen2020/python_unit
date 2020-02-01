def 算π(n):

    π=1

    for i in range(1,n+1,1):
        π=π*((2*i)/(2*i-1))*((2*i)/(2*i+1))
    return π


print(算π(999999)*2)











2