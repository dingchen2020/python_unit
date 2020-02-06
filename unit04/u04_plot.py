import random
import matplotlib.pyplot as plt
myList=[]
for i in range(1000):
    myList.append(random.gauss(25, 5))
plt.hist(myList,50) #按50个区间进行统计
plt.show()
