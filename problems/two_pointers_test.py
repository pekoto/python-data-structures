import unittest
import two_pointers


class TwoPointersTest(unittest.TestCase):

    def test_two_pointers(self):
        self.assertListEqual([1, 3], two_pointers.target_sum([1, 2, 3, 4, 6], 6))  # add assertion here
        self.assertListEqual([0, 2], two_pointers.target_sum([2, 5, 9, 11], 11))  # add assertion here

    def test_remove_duplicates(self):
        self.assertEqual(4, two_pointers.remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
        self.assertEqual(2, two_pointers.remove_duplicates([2, 2, 2, 11]))

    def test_remove_key(self):
        self.assertEqual(4, two_pointers.remove_key([3, 2, 3, 6, 3, 10, 9, 3], 3))
        self.assertEqual(2, two_pointers.remove_key([2, 11, 2, 2, 1], 2))

    def test_square_sorted_array(self):
        self.assertListEqual([0, 1, 4, 4, 9], two_pointers.square_sorted_array([-2, -1, 0, 2, 3]))
        self.assertListEqual([0, 1, 1, 4, 9], two_pointers.square_sorted_array([-3, -1, 0, 1, 2]))

    def test_triplet_sum_to_zero(self):
        self.assertListEqual([[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]],
                             two_pointers.triplet_sum_to_zero([-3, 0, 1, 2, -1, 1, -2]))
        self.assertListEqual([[-5, 2, 3], [-2, -1, 3]],
                             two_pointers.triplet_sum_to_zero([-5, 2, -1, -2, 3]))


if __name__ == '__main__':
    unittest.main()
