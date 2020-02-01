import math
import random

def π(n):
    #y1=random.random(0,2)
    #j=random.random(0,360)
    #y2=random.random(0,2)
    #l=1
    #d=2
    #y1+l*math.sin(j)

    m=0
    for i in range(n):
        ya = random.random() * 2
        angle = random.random() * 360
        yb = ya + math.sin(math.radians(angle))
        if yb<0 or yb>2:
            m=m+1

    return n/m

print(π(99999999))




