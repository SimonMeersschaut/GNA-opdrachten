import random
import time

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
counts = []
step_size = 10
step_count = 200
for n in range(0, step_count*step_size, step_size):
    # array = [i for i in range(n)]
    array = [random.random() for i in range(n)]
    random.shuffle(array)
    counts.append(insertionSort(array, n))


# create plot

import matplotlib.pyplot as plt

# plot experimental data
plt.scatter(range(0, step_count*step_size, step_size), counts, label='Experimentele data', color='blue')
# plot best case
plt.plot(range(0, step_count*step_size, step_size), [(x-1) for x in range(0, step_count*step_size, step_size)], color='green', label='Best case: (n-1)')
# plot average case
plt.plot(range(0, step_count*step_size, step_size), [x*(x-1)/4 for x in range(0, step_count*step_size, step_size)], color='blue', label='Average case: n(n-1)/4')
#
plt.plot(range(0, step_count*step_size, step_size), [x**2/4 for x in range(0, step_count*step_size, step_size)], color='yellow', label='Average case (approx.): n^2/4')
# plot worst case
plt.plot(range(0, step_count*step_size, step_size), [(x**2)/2 for x in range(0, step_count*step_size, step_size)], color='red', label='Worst case: n^2/2')

plt.xlabel("Lengte lijst")
plt.ylabel("Aantal vergelijkingen")
plt.legend()
plt.title("Willekeurige array")
# plt.loglog()
# ax = plt.gca()
# ax.set_aspect('equal', adjustable='box')

print(f"Execution time: {time.time() - time_start}.")
plt.show()