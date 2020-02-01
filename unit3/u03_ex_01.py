def 加密(x):

    s1=x
    s1=str(x)
    s2=len(s1)
    j1=""
    j2 = ""
    j3 = ""
    for i in range(0,s2,3):
        j1+=(s1[i])
    for i in range(1, s2, 3):
        j2+=(s1[i])
    for i in range(2, s2, 3):
        j3+=(s1[i])

    #print(s1[0],s1[0],s1[0])
    print(j1+j2+j3)
    print(j1)
    print(j2)
    print(j3)


加密("abcdef12345")

#'''
def 解密(m):
    mc=len(m)
    yu=len(m)%3
    j=""
    s=mc // 3
    if yu==0:

        m1=(m[0:s])
        m2=(m[s:s*2])
        m3=(m[s*2:mc])
        for i in range(0,mc//3,1):
            j+=(m1[i])+(m2[i])+(m3[i])


    if yu==1:
        m1=(m[0:s+1])
        m2 = (m[s+1:s * 2+1])
        m3 = (m[s * 2+1:mc])
        #print(m1," ",m2," ",m3)
        for i in range(0,mc//3,1):
            j+=(m1[i])+(m2[i])+(m3[i])
        j+=(m1[-1])


    if yu==2:
        m1 = (m[0:s + 1])
        m2 = (m[s + 1:s * 2 + 2])
        m3 = (m[s * 2+2 :mc])
        for i in range(0,mc//3,1):
            j+=(m1[i])+(m2[i])+(m3[i])
        j+=(m1[-1])
        j+=(m2[-1])


    print(j)



#'''
解密("ad14be25cf3")

