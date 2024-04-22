import unittest
import sys
sys.path.append('C:/projects/zaplatynsky_ihor_labs/src')
from max_diameter_in_bt import BinaryTree, binary_tree_diameter

class TestAggressiveCows(unittest.TestCase):
    def test_max_diameter_in_bt_1(self):
        root = BinaryTree(3)
        root.right = BinaryTree(20)
        root.left = BinaryTree(9)
        self.assertEqual(binary_tree_diameter(root), 2)
        
    def test_max_diameter_in_bt_2(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        root.left = BinaryTree(3)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        self.assertEqual(binary_tree_diameter(root), 6)

    def test_max_diameter_in_bt_3(self):
        root = None
        self.assertEqual(binary_tree_diameter(root), 0)

    def test_max_diameter_in_bt_3(self):
        root = BinaryTree(90)
        root.right = BinaryTree(100)
        root.left = BinaryTree(80)
        root.left.right = BinaryTree(70)
        root.left.left = BinaryTree(30)
        root.left.left.left = BinaryTree(22)
        root.left.left.left.left = BinaryTree(21)
        root.left.left.right = BinaryTree(35)
        root.left.left.right.left = BinaryTree(33)
        root.left.left.right.left.right = BinaryTree(34)
        root.left.left.right.left.left = BinaryTree(32)
        root.left.left.right.left.left.left = BinaryTree(31)
        self.assertEqual(binary_tree_diameter(root), 7)
        
if __name__ == '__main__':
    unittest.main()

