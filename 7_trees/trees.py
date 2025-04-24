import random


class Node:
    def __init__(self, value, height=0):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = height

    def add(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value, self.height + 1)
                self.left.parent = self
                return 1
            else:
                return self.left.add(value) + 1
        else:
            if self.right is None:
                self.right = Node(value, self.height + 1)
                self.right.parent = self
                return 1
            else:
                return self.right.add(value) + 1


class Tree:
    def __init__(self, root = None):
        self.root = root
        self.total_height = 0
        self.max_height = 0

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            height = self.root.add(value)
            self.total_height += height
            self.max_height = max(height, self.max_height)

    def delete(self):
        self.root = None
        self.total_height = 0
        self.max_height = 0