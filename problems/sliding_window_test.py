import unittest

from sliding_window import max_sum_subarray


class SlidingWindowTest(unittest.TestCase):

    def test_max_array_sum(self):
        self.assertEqual(9, max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
        self.assertEqual(7, max_sum_subarray([2, 3, 4, 1, 5], 2))


if __name__ == '__main__':
    unittest.main()
