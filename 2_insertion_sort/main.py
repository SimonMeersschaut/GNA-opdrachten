import random

def insertionSort(arr, _):
    telling = 0
    n = len(arr)  # Get the length of the array
     
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            telling += 1
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
    return telling

counts = []
step_size = 5
step_count = 100
for n in range(0, step_count*step_size, step_size):
    array = [i for i in range(n)]
    random.shuffle(array)
    counts.append(insertionSort(array, n))

# create plot

import matplotlib.pyplot as plt

# plot experimental data
plt.scatter(range(0, step_count*step_size, step_size), counts, label='Experimentele data', color='blue')
# plot best case
plt.plot(range(0, step_count*step_size, step_size), [(x-1) for x in range(0, step_count*step_size, step_size)], color='green', label='Best case: (n-1)')
# plot average case
plt.plot(range(0, step_count*step_size, step_size), [x*(x-1)/4 for x in range(0, step_count*step_size, step_size)], color='blue', label='Average case: n(n-1)/2')
# plot worst case
plt.plot(range(0, step_count*step_size, step_size), [(x**2)/2 for x in range(0, step_count*step_size, step_size)], color='red', label='Worst case: n^2/2')

plt.xlabel("Lengte lijst")
plt.ylabel("Aantal vergelijkingen")
plt.legend()
plt.title("Willekeurige array")
plt.loglog()
# ax = plt.gca()
# ax.set_aspect('equal', adjustable='box')
plt.show()