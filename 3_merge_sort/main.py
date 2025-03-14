import math
import random


def mergeSort(arr,count = 0):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]

        countL = mergeSort(L, count)  # Sorting the first half
        countR = mergeSort(R, count)  # Sorting the second half

        count += countL + countR

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            count += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return count

counts = []
step_size = 5
step_count = 100
for n in range(0, step_count*step_size, step_size):
    array = [i for i in range(n)]
    random.shuffle(array)
    counts.append(mergeSort(array))

import matplotlib.pyplot as plt
# plot experimental data
plt.scatter(range(0, step_count*step_size, step_size), counts, label='Experimentele data', color='blue')
# plot best case
plt.plot(range(0, step_count*step_size, step_size), [x*math.log2(x) for x in range(1, step_count*step_size, step_size)], color='red', label='Worst case: n*log(n)')
# plot best case
plt.plot(range(0, step_count*step_size, step_size), [(x/2)*math.log2(x) for x in range(1, step_count*step_size, step_size)], color='green', label='Best case: (n/2)log(n)')
plt.show()