import unittest

from algorithms.counting_sort_simple import counting_sort


class CountingSortSimple(unittest.TestCase):
    def test_counting_sort(self):
        items = [5, 5, 4, 0, 6, 12, 1, 9, 2]

        result = counting_sort(items)

        self.assertListEqual([0, 1, 2, 4, 5, 5, 6, 9, 12], result)


if __name__ == '__main__':
    unittest.main()
