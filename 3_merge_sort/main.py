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

counts = []
step_size = 5
step_count = 100
for n in range(0, step_count*step_size, step_size):
    array = [i for i in range(n)]
    random.shuffle(array)
    counts.append(mergeSort(array))

counts_BC = []
for n in range(0, step_count*step_size, step_size):
    array = [i for i in range(n)]
    counts_BC.append(mergeSort(array))

counts_equals = []
for n in range(0, step_count*step_size, step_size):
    array = [4 for i in range(n)]
    counts_equals.append(mergeSort(array))


import matplotlib.pyplot as plt
# plot experimental data
plt.scatter(range(0, step_count*step_size, step_size), counts, label='Experimentele data average case', color='blue')
plt.scatter(range(0, step_count*step_size, step_size), counts_BC, label='Experimentele data best case', color='green')
# plot best case
plt.plot(range(0, step_count*step_size, step_size), [x*math.log2(x) for x in range(1, step_count*step_size, step_size)], color='red', label='Worst case: n*log(n)')
# plot best case
plt.plot(range(0, step_count*step_size, step_size), [(x/2)*math.log2(x) for x in range(1, step_count*step_size, step_size)], color='green', label='Best case: (n/2)log(n)')
plt.xlabel("Lengte lijst")
plt.ylabel("Aantal vergelijkingen")
plt.legend()
plt.title("complexiteit merge sort")
plt.show()