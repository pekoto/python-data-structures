import unittest

from algorithms.quicksort import quicksort


class QuicksortTest(unittest.TestCase):

    def test_quicksort(self):
        items = [-4, 100, 5, -2, 1, 52, 3, 4]

        quicksort(items)

        self.assertListEqual([-4, -2, 1, 3, 4, 5, 52, 100], items)

    def test_quicksort_even_array(self):
        items = [100, 5, -2, 1, 52, 3, 4]

        quicksort(items)

        self.assertListEqual([-2, 1, 3, 4, 5, 52, 100], items)

    def test_quicksort_already_sorted(self):
        items = [1, 2, 3, 4]

        quicksort(items)

        self.assertListEqual([1, 2, 3, 4], items)


if __name__ == '__main__':
    unittest.main()
