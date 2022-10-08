import unittest

from algorithms.knapsack import knapsack


class KnapsackTest(unittest.TestCase):

    def test_knapsack(self):
        max_weight = 10
        values = [10, 40, 30, 50]
        weights = [5, 4, 6, 3]

        expected_max_value = 90

        actual_max_value = knapsack(max_weight, values, weights)

        self.assertEqual(expected_max_value, actual_max_value)


if __name__ == '__main__':
    unittest.main()
