import unittest
from problems import top_k_elements
from problems.top_k_elements import KthLargestNumber


class TopKElementsTest(unittest.TestCase):
    def test_top_k_numbers(self):
        self.assertListEqual([5, 11, 12], top_k_elements.top_k_numbers([3, 1, 5, 12, 2, 11], 3))
        self.assertListEqual([11, 12, 12], top_k_elements.top_k_numbers([5, 12, 11, -1, 12], 3))

    def test_k_smallest_number(self):
        self.assertEqual(5, top_k_elements.k_smallest_number([1, 5, 12, 2, 11, 5], 3))
        self.assertEqual(5, top_k_elements.k_smallest_number([1, 5, 12, 2, 11, 5], 4))
        self.assertEqual(11, top_k_elements.k_smallest_number([5, 12, 11, -1, 12], 3))

    def test_k_closest_points(self):
        self.assertListEqual([[1, 2]], top_k_elements.k_closest_points([[1, 2], [1, 3]], 1))
        self.assertListEqual([[1, 3], [2, -1]], top_k_elements.k_closest_points([[1, 3], [3, 4], [2, -1]], 2))

    def test_connect_ropes(self):
        self.assertEqual(33, top_k_elements.connect_ropes([1, 3, 11, 5]))
        self.assertEqual(36, top_k_elements.connect_ropes([3, 4, 5, 6]))
        self.assertEqual(42, top_k_elements.connect_ropes([1, 3, 11, 5, 2]))

    def test_top_k_frequent(self):
        self.assertListEqual([11, 12], top_k_elements.top_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2))
        self.assertListEqual([12, 11], top_k_elements.top_k_frequent_numbers([5, 12, 11, 3, 11], 2))

    def test_frequency_sort(self):
        self.assertEqual("ggmmrrPaino", top_k_elements.frequency_sort("Programming"))
        self.assertEqual("bbbaac", top_k_elements.frequency_sort("abcbab"))

    def test_k_largest_number(self):
        largest_number = KthLargestNumber([3, 1, 5, 12, 2, 11], 4)
        self.assertEqual(5, largest_number.add(6))
        self.assertEqual(6, largest_number.add(13))
        self.assertEqual(6, largest_number.add(4))

    def test_k_closest_numbers(self):
        self.assertListEqual([6, 7, 8], top_k_elements.k_closest_numbers([5, 6, 7, 8, 9], 3, 7))
        self.assertListEqual([4, 5, 6], top_k_elements.k_closest_numbers([2, 4, 5, 6, 9], 3, 6))
        self.assertListEqual([5, 6, 9], top_k_elements.k_closest_numbers([2, 4, 5, 6, 9], 3, 10))

    def test_max_distinct_elements(self):
        self.assertEqual(3, top_k_elements.max_distinct_numbers([7, 3, 5, 8, 5, 3, 3], 2))
        self.assertEqual(2, top_k_elements.max_distinct_numbers([3, 5, 12, 11, 12], 3))
        self.assertEqual(3, top_k_elements.max_distinct_numbers([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2))

    def test_sum_of_elements(self):
        self.assertEqual(23, top_k_elements.sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6))
        self.assertEqual(12, top_k_elements.sum_of_elements([3, 5, 8, 7], 1, 4))

    def test_rearrange_string(self):
        self.assertEqual('papap', top_k_elements.rearrange_string('aappp'))
        self.assertEqual('', top_k_elements.rearrange_string('aapa'))
        self.assertEqual('gmrPagimnor', top_k_elements.rearrange_string('Programming'))


if __name__ == '__main__':
    unittest.main()
