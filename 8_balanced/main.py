import matplotlib.pyplot as plt
from random import randint
from red_black_tree import RedBlackTree, Node
import numpy as np
import math

x_values = np.array(range(1, 10000, 25))
y_values = np.empty(len(x_values))

for i, N in enumerate(x_values):
    # create a tree with N values
    tree = RedBlackTree()
    for _ in range(N):
        value = randint(0, N)
        tree.insert(value)
    # get the depth of the tree
    x_values[i] = N
    y_values[i] = tree.get_height()

plt.scatter(x_values, y_values)
plt.plot(x_values, np.log2(x_values), label="log2(x)")
plt.plot(x_values, (np.log(x_values) - math.log(2))/math.log(3), label="log3(x/2)") # = log3(x) - log3(2) = (log(x) - log(2))/log(3)

plt.legend()

plt.show()