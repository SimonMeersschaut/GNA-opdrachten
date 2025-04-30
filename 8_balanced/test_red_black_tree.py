import unittest
from red_black_tree import RedBlackTree, Node

class TestRedBlackTree(unittest.TestCase):

    def setUp(self):
        self.tree = RedBlackTree()

    def test_insert(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(15)
        self.assertEqual(self.tree.root.value, 15)
        self.assertEqual(self.tree.root.right.value, 20)
        self.assertEqual(self.tree.root.left.value, 10)

    def test_balance(self):
        for value in [10, 20, 30, 40, 50]:
            self.tree.insert(value)
        self.assertEqual(self.tree.root.value, 40)
        self.assertEqual(self.tree.root.left.value, 20)
        self.assertEqual(self.tree.root.right.value, 50)

if __name__ == '__main__':
    unittest.main()