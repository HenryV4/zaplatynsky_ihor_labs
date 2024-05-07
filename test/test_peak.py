import unittest
from src.peak import find_the_longest_peak


class TestPeak(unittest.TestCase):
    def test_array_is_sorted_increasinly(self):
        self.assertEqual(find_the_longest_peak([1, 2, 3, 4, 5, 6, 7, 8]), [])

    def test_array_is_sorted_decreasinly(self):
        self.assertEqual(find_the_longest_peak([8, 7, 6, 5, 4, 3, 2, 1]), [])

    def test_array_of_two_el(self):
        self.assertEqual(find_the_longest_peak([3, 5]), [])

    def test_array_with_no_peaks(self):
        self.assertEqual(find_the_longest_peak([1, 1, 1, 1, 1, 1, 1, 1]), [])

    def test_array_with_three_peaks(self):
        self.assertEqual(find_the_longest_peak([1, 2, 1, 2, 1, 2, 1]), [1, 2, 1])

    def test_veres_array(self):
        self.assertEqual(
            find_the_longest_peak([1, 7, 9, 11, 10, 9, 8, 5, 8, 9, 11, 12, 21, 5, 4]),
            [1, 7, 9, 11, 10, 9, 8, 5],
        )


if __name__ == "__main__":
    unittest.main()
