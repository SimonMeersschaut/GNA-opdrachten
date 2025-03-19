import math
import random


def hoare_partition(arr, low, high, count):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        if arr[i] >= pivot:
            count += 1
        while arr[i] < pivot:
            count += 1
            i += 1

        j -= 1
        if arr[j] <= pivot:
            count += 1
        while arr[j] > pivot:
            count += 1
            j -= 1

        if i >= j:
            return j , count


        arr[i], arr[j] = arr[j], arr[i]

def lomuto_partition(arr, low, high, count):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        count += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, count


def quickSortHoare(arr, low, high, count = 0):
    if low < high:
        p, count_part = hoare_partition(arr, low, high, count)
        countL = quickSortHoare(arr, low, p, count)
        countR = quickSortHoare(arr, p + 1, high, count)
        return countL + countR + count_part
    return count

def quickSortLomuto(arr, low, high, count = 0):
    if low < high:
        p, count = lomuto_partition(arr, low, high, count)
        countL = quickSortLomuto(arr, low, p - 1)
        countR = quickSortLomuto(arr, p + 1, high)
        return countL + countR + count
    return count



counts = []
step_size = 50
step_count = 200
for n in range(0, step_count*step_size, step_size):
    array = [i for i in range(n)]
    random.shuffle(array)
    counts.append(quickSortHoare(array, 0, len(array) - 1))

counts_l = []
for n in range(0, step_count*step_size, step_size):
    array = [i for i in range(n)]
    random.shuffle(array)
    counts_l.append(quickSortLomuto(array, 0, len(array) - 1))

import matplotlib.pyplot as plt
# plot experimental data
plt.scatter(range(0, step_count*step_size, step_size), counts, label='Experimentele data Hoare', color='blue')
plt.scatter(range(0, step_count*step_size, step_size), counts_l, label='Experimentele data Lomuto', color='yellow')
#plt.plot(range(0, step_count*step_size, step_size), [(x**2)/2 for x in range(1, step_count*step_size, step_size)], color='red', label='Best case: (n/2)log(n)')
plt.plot(range(0, step_count*step_size, step_size), [1.39*x*math.log2(x) for x in range(1, step_count*step_size, step_size)], color='blue', label='Best case: 1,39*nlog(n)')
plt.plot(range(0, step_count*step_size, step_size), [x*math.log2(x) for x in range(1, step_count*step_size, step_size)], color='green', label='Best case: nlog(n)')
plt.xlabel("Lengte lijst")
plt.ylabel("Aantal vergelijkingen")
plt.legend()
plt.title("complexiteit quicksort")
plt.loglog()
plt.show()