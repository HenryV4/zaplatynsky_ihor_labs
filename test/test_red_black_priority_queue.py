import unittest
import sys
sys.path.append('C:/projects/zaplatynsky_ihor_labs/src')
from red_black_priority_queue import RedBlackPriorityQueue


class TestRedBlackPriorityQueue(unittest.TestCase):

    def test_priority_queue(self):
        pq = RedBlackPriorityQueue()
        pq.insert(1, 10)
        pq.insert(3, 5)
        pq.insert(4, 7)
        pq.insert(6, 11)
        pq.insert(2, 8)
        self.assertEqual(pq.delete_max(), 6)

    def test_empty_tree(self):
        pq = RedBlackPriorityQueue()
        self.assertEqual(pq.delete_max(), None)

    def test_deleteng_same(self):
        pq = RedBlackPriorityQueue()
        pq.insert(1, 1)
        pq.insert(1, 1)
        pq.insert(1, 1)
        pq.insert(1, 1)
        pq.insert(1, 1)
        self.assertEqual(pq.delete_max(), 1)


if __name__ == '__main__':
    unittest.main()


