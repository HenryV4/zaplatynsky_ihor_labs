import unittest
import sys
sys.path.append('C:/WORK/PROG/2/lab2/srt')
from aggresive_cows import aggresive_cows

class TestAggressiveCows(unittest.TestCase):
    def test_aggressive_cows(self):
        self.assertEqual(aggresive_cows([1, 2, 8, 4, 9], 3), 3)

if __name__ == '__main__':
    unittest.main()

