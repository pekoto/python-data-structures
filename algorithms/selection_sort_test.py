import unittest

from algorithms.selection_sort import selection_sort


class SelectionSortTest(unittest.TestCase):

    def test_selection_sort(self):
        items = [-4, 2, 4, 100, 5, 6, 99]

        selection_sort(items)

        self.assertListEqual([-4, 2, 4, 5, 6, 99, 100], items)


if __name__ == '__main__':
    unittest.main()
