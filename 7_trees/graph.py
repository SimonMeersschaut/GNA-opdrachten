from trees import Tree
import random
import matplotlib.pyplot as plt
import math

t = Tree()

total_heights =[]
average_heights =[]
max_heights =[]

N = 1000


for i in range(1, N):
    t.delete()
    random_list = [i for i in range(i)]
    random.shuffle(random_list)
    for j in random_list:
        t.add(j)
    total_heights.append(t.total_height)
    average_heights.append(t.total_height/i)
    max_heights.append(t.max_height)

plt.scatter(list(range(1, N)), total_heights, label='Comparisons Heap', color='blue')
plt.plot(list(range(1, N)), [x*math.log2(x) for x in range(1, N)], label='Comparisons Heap', color='red')

#plt.scatter(list(range(1, N)), average_heights, label='Comparisons Heap', color='blue')
#plt.plot(list(range(1, N)), [math.log2(x) for x in range(1, N)], label='Comparisons Heap', color='red')

#plt.scatter(list(range(1, N)), max_heights, label='Comparisons Heap', color='blue')



plt.show()