import unittest

from sliding_window import max_sum_subarray, smallest_sum_subarray, k_distinct_chars


class SlidingWindowTest(unittest.TestCase):

    def test_max_array_sum(self):
        self.assertEqual(9, max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
        self.assertEqual(7, max_sum_subarray([2, 3, 4, 1, 5], 2))

    def test_smallest_sum_subarray(self):
        self.assertEqual(2, smallest_sum_subarray([2, 1, 5, 2, 3, 2], 7))
        self.assertEqual(1, smallest_sum_subarray([2, 1, 5, 2, 8], 7))
        self.assertEqual(3, smallest_sum_subarray([3, 4, 1, 1, 6], 8))

    def test_k_distinct_chars(self):
        self.assertEqual(4, k_distinct_chars("araaci", 2))
        self.assertEqual(2, k_distinct_chars("araaci", 1))
        self.assertEqual(5, k_distinct_chars("cbbebi", 3))


if __name__ == '__main__':
    unittest.main()
