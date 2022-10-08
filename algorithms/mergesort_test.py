import unittest

from algorithms.mergesort import mergesort


class MergesortTest(unittest.TestCase):

    def test_mergesort(self):
        items = [-4, 2, 4, 100, 5, 6, 99]

        items = mergesort(items)

        self.assertListEqual([-4, 2, 4, 5, 6, 99, 100], items)


if __name__ == '__main__':
    unittest.main()
