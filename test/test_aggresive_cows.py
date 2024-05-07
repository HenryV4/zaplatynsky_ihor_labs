import sys
import unittest

from src.aggresive_cows import aggresive_cows


class TestAggressiveCows(unittest.TestCase):
    def test_aggressive_cows_1(self):
        self.assertEqual(aggresive_cows([1, 2, 8, 4, 9], 3), 3)

    def test_aggressive_cows_2(self):
        self.assertEqual(aggresive_cows([1, 1, 1, 1, 1, 1], 3), 0)

    def test_aggressive_cows_3(self):
        self.assertEqual(aggresive_cows([2, 3, 4, 5, 6, 7], 9), 0)


if __name__ == "__main__":
    unittest.main()
