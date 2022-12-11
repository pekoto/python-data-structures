import unittest

from problems import modified_binary_search


class ModifiedBinarySearchTest(unittest.TestCase):
    def test_order_agnostic_binary_search(self):
        self.assertEqual(2, modified_binary_search.order_agnostic_binary_search([4, 6, 10], 10))
        self.assertEqual(4, modified_binary_search.order_agnostic_binary_search([1, 2, 3, 4, 5, 6, 7], 5))
        self.assertEqual(0, modified_binary_search.order_agnostic_binary_search([10, 6, 4], 10))
        self.assertEqual(2, modified_binary_search.order_agnostic_binary_search([10, 6, 4], 4))

    def test_ceiling_number(self):
        self.assertEqual(1, modified_binary_search.ceiling_number([4, 6, 10], 6))
        self.assertEqual(4, modified_binary_search.ceiling_number([1, 3, 8, 10, 15], 12))
        self.assertEqual(-1, modified_binary_search.ceiling_number([4, 6, 10], 17))
        self.assertEqual(0, modified_binary_search.ceiling_number([4, 6, 10], -1))

    def test_next_letter(self):
        self.assertEqual("h", modified_binary_search.next_letter(["a", "c", "f", "h"], "f"))
        self.assertEqual("c", modified_binary_search.next_letter(["a", "c", "f", "h"], "b"))
        self.assertEqual("a", modified_binary_search.next_letter(["a", "c", "f", "h"], "m"))
        self.assertEqual("a", modified_binary_search.next_letter(["a", "c", "f", "h"], "h"))

    def test_number_range(self):
        self.assertListEqual([1, 3], modified_binary_search.number_range([4, 6, 6, 6, 9], 6))
        self.assertListEqual([3, 3], modified_binary_search.number_range([1, 3, 8, 10, 15], 10))
        self.assertListEqual([-1, -1], modified_binary_search.number_range([1, 3, 8, 10, 15], 12))

    def test_min_difference(self):
        self.assertEqual(6, modified_binary_search.min_difference([4, 6, 10], 7))
        self.assertEqual(4, modified_binary_search.min_difference([4, 6, 10], 4))
        self.assertEqual(10, modified_binary_search.min_difference([4, 6, 10], 17))
        self.assertEqual(10, modified_binary_search.min_difference([4, 6, 10, 15], 12))

    def test_bitonic_array_maximum(self):
        self.assertEqual(12, modified_binary_search.bitonic_array_maximum([1, 3, 8, 12, 4, 2]))
        self.assertEqual(8, modified_binary_search.bitonic_array_maximum([3, 8, 3, 1]))
        self.assertEqual(12, modified_binary_search.bitonic_array_maximum([1, 3, 8, 12]))
        self.assertEqual(10, modified_binary_search.bitonic_array_maximum([10, 9, 8]))

    def test_search_bitonic_array(self):
        self.assertEqual(3, modified_binary_search.search_bitonic_array([1, 3, 8, 4, 3], 4))
        self.assertEqual(1, modified_binary_search.search_bitonic_array([3, 8, 3, 1], 8))
        self.assertEqual(3, modified_binary_search.search_bitonic_array([1, 3, 8, 12], 12))
        self.assertEqual(0, modified_binary_search.search_bitonic_array([10, 9, 8], 10))

    def test_search_rotated_array(self):
        self.assertEqual(1, modified_binary_search.search_rotated_array([10, 15, 1, 3, 8], 15))
        self.assertEqual(4, modified_binary_search.search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

    def test_rotation_point(self):
        self.assertEqual(2, modified_binary_search.rotation_count([10, 15, 1, 3, 8]))
        self.assertEqual(5, modified_binary_search.rotation_count([4, 5, 7, 9, 10, -1, 2]))
        self.assertEqual(0, modified_binary_search.rotation_count([1, 3, 8, 10]))


if __name__ == '__main__':
    unittest.main()
