import unittest
from problems import dynamic_fibonacci


class DynamicFibonacciTest(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(3, dynamic_fibonacci.fibonacci(4))

    def test_fibonacci_topdown(self):
        self.assertEqual(3, dynamic_fibonacci.fibonacci_topdown(4))

    def test_fibonacci_bottomup(self):
        self.assertEqual(3, dynamic_fibonacci.fibonacci_bottomup(4))

    def test_staircase(self):
        self.assertEqual(4, dynamic_fibonacci.staircase(3))
        self.assertEqual(7, dynamic_fibonacci.staircase(4))

    def test_staircase_topdown(self):
        self.assertEqual(4, dynamic_fibonacci.staircase_topdown(3))
        self.assertEqual(7, dynamic_fibonacci.staircase_topdown(4))

    def test_staircase_bottomup(self):
        self.assertEqual(4, dynamic_fibonacci.staircase_bottomup(3))
        self.assertEqual(7, dynamic_fibonacci.staircase_bottomup(4))

    def test_number_factors(self):
        self.assertEqual(4, dynamic_fibonacci.number_factors(4))
        self.assertEqual(6, dynamic_fibonacci.number_factors(5))

    def test_number_factors_topdown(self):
        self.assertEqual(4, dynamic_fibonacci.number_factors_topdown(4))
        self.assertEqual(6, dynamic_fibonacci.number_factors_topdown(5))

    def test_number_factors_bottomup(self):
        self.assertEqual(4, dynamic_fibonacci.number_factors_bottomup(4))
        self.assertEqual(6, dynamic_fibonacci.number_factors_bottomup(5))

    def test_minimum_jumps(self):
        self.assertEqual(3, dynamic_fibonacci.minimum_jumps([2, 1, 1, 1, 4]))
        self.assertEqual(4, dynamic_fibonacci.minimum_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))

    def test_minimum_jumps_topdown(self):
        self.assertEqual(3, dynamic_fibonacci.minimum_jumps_topdown([2, 1, 1, 1, 4]))
        self.assertEqual(4, dynamic_fibonacci.minimum_jumps_topdown([1, 1, 3, 6, 9, 3, 0, 1, 3]))

    def test_minimum_jumps_bottomup(self):
        self.assertEqual(3, dynamic_fibonacci.minimum_jumps_bottomup([2, 1, 1, 1, 4]))
        self.assertEqual(4, dynamic_fibonacci.minimum_jumps_bottomup([1, 1, 3, 6, 9, 3, 0, 1, 3]))

    def test_minimum_jumps_with_fee(self):
        self.assertEqual(3, dynamic_fibonacci.minimum_jumps_with_fee([1, 2, 5, 2, 1, 2]))
        self.assertEqual(5, dynamic_fibonacci.minimum_jumps_with_fee([2, 3, 4, 5]))

    def test_minimum_jumps_with_fee_topdown(self):
        self.assertEqual(3, dynamic_fibonacci.minimum_jumps_with_fee_topdown([1, 2, 5, 2, 1, 2]))
        self.assertEqual(5, dynamic_fibonacci.minimum_jumps_with_fee_topdown([2, 3, 4, 5]))

    def test_minimum_jumps_with_fee_bottomup(self):
        self.assertEqual(3, dynamic_fibonacci.minimum_jumps_with_fee_bottomup([1, 2, 5, 2, 1, 2]))
        self.assertEqual(5, dynamic_fibonacci.minimum_jumps_with_fee_bottomup([2, 3, 4, 5]))

    def test_house_thief(self):
        self.assertEqual(8, dynamic_fibonacci.house_thief([2, 5, 1, 3]))
        self.assertEqual(15, dynamic_fibonacci.house_thief([2, 5, 1, 3, 6, 2, 4]))
        self.assertEqual(18, dynamic_fibonacci.house_thief([2, 10, 14, 8, 1]))

    def test_house_thief_topdown(self):
        self.assertEqual(8, dynamic_fibonacci.house_thief_topdown([2, 5, 1, 3]))
        self.assertEqual(15, dynamic_fibonacci.house_thief_topdown([2, 5, 1, 3, 6, 2, 4]))
        self.assertEqual(18, dynamic_fibonacci.house_thief_topdown([2, 10, 14, 8, 1]))

    def test_house_thief_bottomup(self):
        self.assertEqual(8, dynamic_fibonacci.house_thief_bottomup([2, 5, 1, 3]))
        self.assertEqual(15, dynamic_fibonacci.house_thief_bottomup([2, 5, 1, 3, 6, 2, 4]))
        self.assertEqual(18, dynamic_fibonacci.house_thief_bottomup([2, 10, 14, 8, 1]))


if __name__ == '__main__':
    unittest.main()
