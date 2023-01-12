import unittest
import knapsack


class KnapsackTest(unittest.TestCase):
    def test_knapsack(self):
        self.assertEqual(16, knapsack.knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))

    def test_equal_subset_partition(self):
        self.assertTrue(knapsack.equal_subset_partition([1, 2, 3, 4]))
        self.assertTrue(knapsack.equal_subset_partition([1, 1, 3, 4, 7]))
        self.assertFalse(knapsack.equal_subset_partition([2, 3, 4, 6]))

    def test_subset_sum(self):
        self.assertTrue(knapsack.subset_sum([1, 2, 3, 7], 6))
        self.assertTrue(knapsack.subset_sum([1, 2, 7, 1, 5], 10))
        self.assertFalse(knapsack.subset_sum([1, 3, 4, 8], 6))

    def test_minimum_subsets(self):
        self.assertEqual(3, knapsack.minimum_subsets([1, 2, 3, 9]))
        self.assertEqual(0, knapsack.minimum_subsets([1, 2, 7, 1, 5]))
        self.assertEqual(92, knapsack.minimum_subsets([1, 3, 100, 4]))

    def test_count_subset_sum(self):
        self.assertEqual(3, knapsack.count_subset_sum([1, 1, 2, 3], 4))
        self.assertEqual(3, knapsack.count_subset_sum([1, 2, 7, 1, 5], 9))


if __name__ == '__main__':
    unittest.main()
