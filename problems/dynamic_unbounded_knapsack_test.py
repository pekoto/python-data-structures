import unittest

from problems import dynamic_unbounded_knapsack


class DynamicUnboundedKnapsackTest(unittest.TestCase):
    def test_unbounded_knapsack(self):
        self.assertEqual(80, dynamic_unbounded_knapsack.unbounded_knapsack([15, 20, 50], [1, 2, 3], 5))

    def test_unbounded_knapsack_topdown(self):
        self.assertEqual(80, dynamic_unbounded_knapsack.unbounded_knapsack_topdown([15, 20, 50], [1, 2, 3], 5))

    def test_unbounded_knapsack_bottomup(self):
        self.assertEqual(80, dynamic_unbounded_knapsack.unbounded_knapsack_bottomup([15, 20, 50], [1, 2, 3], 5))

    def test_rod_cutting(self):
        self.assertEqual(14, dynamic_unbounded_knapsack.rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))

    def test_rod_cutting_topdown(self):
        self.assertEqual(14, dynamic_unbounded_knapsack.rod_cutting_topdown([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))

    def test_rod_cutting_bottomup(self):
        self.assertEqual(14, dynamic_unbounded_knapsack.rod_cutting_bottomup([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))

    def test_coin_change(self):
        self.assertEqual(5, dynamic_unbounded_knapsack.coin_change([1, 2, 3], 5))

    def test_coin_change_topdown(self):
        self.assertEqual(5, dynamic_unbounded_knapsack.coin_change_topdown([1, 2, 3], 5))

    def test_coin_change_bottomup(self):
        self.assertEqual(5, dynamic_unbounded_knapsack.coin_change_bottomup([1, 2, 3], 5))

    def test_minimum_coin_change(self):
        self.assertEqual(2, dynamic_unbounded_knapsack.minimum_coin_change([1, 2, 3], 5))

    def test_minimum_coin_change_topdown(self):
        self.assertEqual(2, dynamic_unbounded_knapsack.minimum_coin_change_topdown([1, 2, 3], 5))

    def test_minimum_coin_change_bottomup(self):
        self.assertEqual(2, dynamic_unbounded_knapsack.minimum_coin_change_bottomup([1, 2, 3], 5))

    def test_maximum_ribbon_cut(self):
        self.assertEqual(2, dynamic_unbounded_knapsack.maximum_ribbon_cut([2, 3, 5], 5))

    def test_maximum_ribbon_cut_bottomup(self):
        self.assertEqual(2, dynamic_unbounded_knapsack.maximum_ribbon_cut_bottomup([2, 3, 5], 5))


if __name__ == '__main__':
    unittest.main()
