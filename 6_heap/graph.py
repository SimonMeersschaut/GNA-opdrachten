import matplotlib.pyplot as plt
from heap import Heap
import random
import math

N = 256000

comparisons_list = []
h = Heap()

for i in range(N):
    h.add(random.randint(0, N))
    comparisons_list.append(h.grab_count())

# # plot experimental data
plt.scatter(list(range(N)), comparisons_list, label='Comparisons Heap', color='blue')

plt.plot(list(range(1, N)), [1+int(math.log2(x)) for x in range(1, N)], label='Comparisons Heap', color='red')
# #
plt.show()


##########
# delete maximum
##########

comparisons_list = []

for i in range(N):
    h.delete_max()
    comparisons_list.append(h.grab_count())

plt.scatter(list(range(N)), comparisons_list, label='Comparisons Heap (delete max)', color='blue')

plt.plot(list(range(1, N)), [2*int(math.log2(N - x)) for x in range(1, N)], label='Comparisons Heap', color='red')
#
plt.show()
