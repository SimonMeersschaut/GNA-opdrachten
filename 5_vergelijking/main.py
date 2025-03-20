import random
import time
import math

def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]): # i is the index of the previous element
            return False
    return True


def insertionSort(arr, _):
    telling = 0
    n = len(arr)  # Get the length of the array
     
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0:  # Move elements greater than key one position ahead
            telling += 1
            if key < arr[j]:
                arr[j+1] = arr[j]  # Shift elements to the right
                j -= 1
            else:
                break
        arr[j+1] = key  # Insert the key in the correct position
    assert is_sorted(arr)
    return telling


time_start = time.time()

# counts = []
IS_counts = []
IS_step_size = 10
IS_step_count = 200
for n in range(0, IS_step_count*IS_step_size, IS_step_size):
    # array = [i for i in range(n)]
    array = [random.random() for i in range(n)]
    random.shuffle(array)
    IS_counts.append(insertionSort(array, n))


# create plot

import matplotlib.pyplot as plt

# plot experimental data
plt.scatter(range(0, IS_step_count*IS_step_size, IS_step_size), IS_counts, label='IS: Experimentele data', color='blue')
# plot best case
plt.plot(range(0, IS_step_count*IS_step_size, IS_step_size), [(x-1) for x in range(0, IS_step_count*IS_step_size, IS_step_size)], color='green', label='IS: Best case: (n-1)')
# plot average case
plt.plot(range(0, IS_step_count*IS_step_size, IS_step_size), [x*(x-1)/4 for x in range(0, IS_step_count*IS_step_size, IS_step_size)], color='blue', label='IS: Average case: n(n-1)/4')
#
plt.plot(range(0, IS_step_count*IS_step_size, IS_step_size), [x**2/4 for x in range(0, IS_step_count*IS_step_size, IS_step_size)], color='yellow', label='IS: Average case (approx.): n^2/4')
# plot worst case
plt.plot(range(0, IS_step_count*IS_step_size, IS_step_size), [(x**2)/2 for x in range(0, IS_step_count*IS_step_size, IS_step_size)], color='red', label='IS: Worst case: n^2/2')

###############################3



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

MS_counts = []
MS_step_size = 1000
MS_step_count = 50
for n in range(0, MS_step_count*MS_step_size, MS_step_size):
    array = [i*1000 for i in range(n)]
    random.shuffle(array)
    MS_counts.append(mergeSort(array))

MS_counts_BC = []
for n in range(0, MS_step_count*MS_step_size, MS_step_size):
    array = [i*1000 for i in range(n)]
    MS_counts_BC.append(mergeSort(array))

# counts_equals = []
# for n in range(0, step_count*step_size, step_size):
#     array = [4 for i in range(n)]
#     counts_equals.append(mergeSort(array))

# print(f"Sorteren duurde {time.time() - start_tijd} seconden.")

import matplotlib.pyplot as plt
# plot experimental data
plt.scatter(range(0, MS_step_count*MS_step_size, MS_step_size), MS_counts, label='MS: Experimentele data average case', color='blue')
plt.scatter(range(0, MS_step_count*MS_step_size, MS_step_size), MS_counts_BC, label='MS: Experimentele data best case', color='green')
# plot best case
plt.plot(range(0, MS_step_count*MS_step_size, MS_step_size), [x*math.log2(x) for x in range(1, MS_step_count*MS_step_size, MS_step_size)], color='red', label='MS: Worst case: n*log(n)')
#plot average casE?
plt.plot(range(0, MS_step_count*MS_step_size, MS_step_size), [(x)*math.log2(x)-(x-1) for x in range(1, MS_step_count*MS_step_size, MS_step_size)], color='blue', label='MS: Average case: nlog(n)- (n-1)')
# plot best case
plt.plot(range(0, MS_step_count*MS_step_size, MS_step_size), [(x/2)*math.log2(x) for x in range(1, MS_step_count*MS_step_size, MS_step_size)], color='green', label='MS: Best case: (n/2)log(n)')


############################



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



QS_counts = []
QS_step_size = 100
QS_step_count = 500
for n in range(0, QS_step_count*QS_step_size, QS_step_size):
    array = [i for i in range(n)]
    random.shuffle(array)
    QS_counts.append(quickSortHoare(array, 0, len(array) - 1))

QS_counts_l = []
for n in range(0, QS_step_count*QS_step_size, QS_step_size):
    array = [i for i in range(n)]
    random.shuffle(array)
    QS_counts_l.append(quickSortLomuto(array, 0, len(array) - 1))

import matplotlib.pyplot as plt
# plot experimental data
plt.scatter(range(0, QS_step_count*QS_step_size, QS_step_size), QS_counts, label='QS: Experimentele data Hoare', color='blue')
plt.scatter(range(0, QS_step_count*QS_step_size, QS_step_size), QS_counts_l, label='QS: Experimentele data Lomuto', color='yellow')
#plt.plot(range(0, step_count*step_size, step_size), [(x**2)/2 for x in range(1, step_count*step_size, step_size)], color='red', label='Best case: (n/2)log(n)')
plt.plot(range(0, QS_step_count*QS_step_size, QS_step_size), [1.39*x*math.log2(x) for x in range(1, QS_step_count*QS_step_size, QS_step_size)], color='blue', label='QS: Best case: 1,39*nlog(n)')
plt.plot(range(0, QS_step_count*QS_step_size, QS_step_size), [x*math.log2(x) for x in range(1, QS_step_count*QS_step_size, QS_step_size)], color='green', label='QS: Best case: nlog(n)')


#####


print(f"Execution time: {time.time() - time_start}.")
plt.legend()
plt.show()