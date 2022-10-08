import unittest

from algorithms.counting_sort import counting_sort


class CountingSortTest(unittest.TestCase):

    def test_counting_sort(self):
        items = [5, 5, 4, 0, 6, 12, 1, 9, 2]

        counting_sort(items)

        self.assertListEqual([0, 1, 2, 4, 5, 5, 6, 9, 12], items)


if __name__ == '__main__':
    unittest.main()
