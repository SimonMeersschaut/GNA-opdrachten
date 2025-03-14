def selectionSort(array, size):
    telling = 0
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            telling += 1
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
    return telling


counts = []
step_size = 5
step_count = 100
for n in range(0, step_count*step_size, step_size):
    array = [i for i in range(n)]
    counts.append(selectionSort(array, n))

# create plot

import matplotlib.pyplot as plt

# plot experimental data
plt.scatter(range(0, step_count*step_size, step_size), counts, label='Experimentele data')
# plot n(n-1)/2
plt.plot(range(0, step_count*step_size, step_size), [x*(x-1)/2 for x in range(0, step_count*step_size, step_size)], color='r', label='n(n-1)/2')
# plot n^2/2
plt.plot(range(0, step_count*step_size, step_size), [(x**2)/2 for x in range(0, step_count*step_size, step_size)], color='b', label='n^2/2')

plt.xlabel("Lengte lijst")
plt.ylabel("Aantal vergelijkingen")
plt.legend()
plt.loglog()
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
plt.show()