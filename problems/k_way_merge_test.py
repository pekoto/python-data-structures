import unittest
import k_way_merge


class KWayMergeTest(unittest.TestCase):
    def test_merge_k_sorted_lists(self):
        self.assertListEqual([1, 2, 3, 3, 4, 6, 6, 7, 8], k_way_merge.merge_k_sorted_lists(
            [[2, 6, 8], [3, 6, 7], [1, 3, 4]]
        ))

        self.assertListEqual([1, 5, 7, 8, 9], k_way_merge.merge_k_sorted_lists(
            [[5, 8, 9], [1, 7]]
        ))

    def test_kth_smallest_number(self):
        self.assertEqual(4, k_way_merge.kth_smallest_number([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5))
        self.assertEqual(7, k_way_merge.kth_smallest_number([[5, 8, 9], [1, 7]], 3))

    def test_kth_smallest_number_in_matrix(self):
        matrix = [
            [2, 6, 8],
            [3, 7, 10],
            [5, 8, 11],
        ]

        self.assertEqual(7, k_way_merge.kth_smallest_number_in_matrix(matrix, 5))

    def test_smallest_number_range(self):
        self.assertEqual(
            [4, 7],
            k_way_merge.smallest_number_range([[1, 5, 8], [4, 12], [7, 8, 10]]))
        self.assertEqual(
            [9, 12],
            k_way_merge.smallest_number_range([[1, 9], [4, 12], [7, 10, 16]]))

    def test_k_pairs_largest_sums(self):
        self.assertEqual([[9, 3], [9, 6], [8, 6]], k_way_merge.k_pairs_largest_sums([9, 8, 2], [6, 3, 1], 3))
        self.assertEqual([[5, -1], [5, 2], [2, 2]], k_way_merge.k_pairs_largest_sums([5, 2, 1], [2, -1], 3))


if __name__ == '__main__':
    unittest.main()
