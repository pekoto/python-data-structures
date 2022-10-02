import unittest

from algorithms.insertion_sort import insertion_sort


class InsertionSortTest(unittest.TestCase):

    def test_insertion_sort(self):
        items = [89, -3, 100, 5, 10, 11, 2, -3]

        insertion_sort(items)

        self.assertListEqual([-3, -3, 2, 5, 10, 11, 89, 100], items)


if __name__ == '__main__':
    unittest.main()
