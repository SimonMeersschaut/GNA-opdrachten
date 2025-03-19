import math
import random
import time

def mergeSort(arr,count = 0):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]

        countL = mergeSort(L, count)  # Sorting the first half
        countR = mergeSort(R, count)  # Sorting the second half

        count += countL + countR

        i = j = k = 0

        while i < len(L) and j < len(R):
            count += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return count

start_tijd = time.time()

counts = []
step_size = 1000
step_count = 50
for n in range(0, step_count*step_size, step_size):
    array = [i*1000 for i in range(n)]
    random.shuffle(array)
    counts.append(mergeSort(array))

counts_BC = []
for n in range(0, step_count*step_size, step_size):
    array = [i*1000 for i in range(n)]
    counts_BC.append(mergeSort(array))

# counts_equals = []
# for n in range(0, step_count*step_size, step_size):
#     array = [4 for i in range(n)]
#     counts_equals.append(mergeSort(array))

# print(f"Sorteren duurde {time.time() - start_tijd} seconden.")

import matplotlib.pyplot as plt
# plot experimental data
plt.scatter(range(0, step_count*step_size, step_size), counts, label='Experimentele data average case', color='blue')
plt.scatter(range(0, step_count*step_size, step_size), counts_BC, label='Experimentele data best case', color='green')
# plot best case
plt.plot(range(0, step_count*step_size, step_size), [x*math.log2(x) for x in range(1, step_count*step_size, step_size)], color='red', label='Worst case: n*log(n)')
#plot average casE?
plt.plot(range(0, step_count*step_size, step_size), [(x)*math.log2(x)-(x-1) for x in range(1, step_count*step_size, step_size)], color='blue', label='Average case: nlog(n)- (n-1)')
# plot best case
plt.plot(range(0, step_count*step_size, step_size), [(x/2)*math.log2(x) for x in range(1, step_count*step_size, step_size)], color='green', label='Best case: (n/2)log(n)')
plt.xlabel("Lengte lijst")
plt.ylabel("Aantal vergelijkingen")
plt.legend()
plt.title("complexiteit merge sort")
# plt.loglog()
# ax = plt.gca()
# ax.set_aspect('equal', adjustable='box')
plt.show()