RED = True
BLACK = False

class Node:
    def __init__(self, value, color=RED):
        self.value = value
        self.color = color
        self.left = None
        self.right = None

def is_red(node):
    return node is not None and node.color == RED

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)
        self.root.color = BLACK

    def _insert(self, h, value):
        if h is None:
            return Node(value, RED)

        if value < h.value:
            h.left = self._insert(h.left, value)
        elif value > h.value:
            h.right = self._insert(h.right, value)
        # else: ignore duplicates

        # Rotate left if right-leaning red link
        if is_red(h.right) and not is_red(h.left):
            h = self._rotate_left(h)

        # Rotate right if two left-leaning red links in a row
        if is_red(h.left) and is_red(h.left.left):
            h = self._rotate_right(h)

        # Color flip
        if is_red(h.left) and is_red(h.right):
            self._flip_colors(h)

        return h

    def _rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x

    def _rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x

    def _flip_colors(self, h):
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK

    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return -1
        depth_left = self._get_height(node.left)
        depth_right = self._get_height(node.right)
        if node.color == BLACK:
            return 1 + max(depth_left, depth_right)
        else: # red
            return max(depth_left, depth_right)