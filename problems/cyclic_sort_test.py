import unittest
import cyclic_sort


class CyclicSortTest(unittest.TestCase):

    def test_cyclic_sort(self):
        l = [3, 1, 5, 4, 2]
        cyclic_sort.cyclic_sort_a(l)
        self.assertListEqual([1, 2, 3, 4, 5], l)

        l = [1, 5, 6, 4, 3, 2]
        cyclic_sort.cyclic_sort_a(l)
        self.assertListEqual([1, 2, 3, 4, 5, 6], l)

        l = [2, 6, 4, 3, 1, 5]
        cyclic_sort.cyclic_sort_a(l)
        self.assertListEqual([1, 2, 3, 4, 5, 6], l)

    def test_find_missing(self):
        self.assertEqual(2, cyclic_sort.find_missing([4, 0, 3, 1]))
        self.assertEqual(7, cyclic_sort.find_missing([8, 3, 5, 2, 4, 6, 0, 1]))

    def test_find_missing_numbers(self):
        self.assertListEqual([4, 6, 7], cyclic_sort.find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
        self.assertListEqual([3], cyclic_sort.find_missing_numbers([2, 4, 1, 2]))
        self.assertListEqual([4], cyclic_sort.find_missing_numbers([2, 3, 2, 1]))

    def test_find_duplicate_number(self):
        self.assertEqual(4, cyclic_sort.find_duplicate_number([1, 4, 4, 3, 2]))
        self.assertEqual(3, cyclic_sort.find_duplicate_number([2, 1, 3, 3, 5, 4]))
        self.assertEqual(4, cyclic_sort.find_duplicate_number([2, 4, 1, 4, 4]))

    def test_find_duplicate_numbers(self):
        self.assertListEqual([5, 4], cyclic_sort.find_duplicate_numbers([3, 4, 4, 5, 5]))
        self.assertListEqual([3, 5], cyclic_sort.find_duplicate_numbers([5, 4, 7, 2, 3, 5, 3]))

    def test_find_corrupt_pair(self):
        self.assertListEqual([2, 4], cyclic_sort.find_corrupt_pair([3, 1, 2, 5, 2]))
        self.assertListEqual([3, 5], cyclic_sort.find_corrupt_pair([3, 1, 2, 3, 6, 4]))

    def test_find_smallest_missing_number(self):
        self.assertEqual(3, cyclic_sort.find_smallest_missing_number([-3, 1, 5, 4, 2]))
        self.assertEqual(4, cyclic_sort.find_smallest_missing_number([3, -2, 0, 1, 2]))
        self.assertEqual(4, cyclic_sort.find_smallest_missing_number([3, 2, 5, 1]))
        self.assertEqual(1, cyclic_sort.find_smallest_missing_number([33, 37, 5]))

    def test_find_smallest_missing_k_numbers(self):
        self.assertListEqual([1, 2, 6], cyclic_sort.find_smallest_missing_k_numbers([3, -1, 4, 5, 5], 3))
        self.assertListEqual([1, 5, 6], cyclic_sort.find_smallest_missing_k_numbers([2, 3, 4], 3))
        self.assertListEqual([1, 2], cyclic_sort.find_smallest_missing_k_numbers([-2, -3, 4], 2))


if __name__ == '__main__':
    unittest.main()
