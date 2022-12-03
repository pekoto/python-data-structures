import unittest

from problems.two_heaps import NumberStreamMedian
import two_heaps


class TwoHeapsTest(unittest.TestCase):

    def test_NumberStreamMedian(self):
        number_stream_median = NumberStreamMedian()
        number_stream_median.insert_num(3)
        number_stream_median.insert_num(1)

        self.assertEqual(2, number_stream_median.find_median())

        number_stream_median.insert_num(5)

        self.assertEqual(3, number_stream_median.find_median())

        number_stream_median.insert_num(4)

        self.assertEqual(3.5, number_stream_median.find_median())

    def test_maximize_capital(self):
        capitals = [0, 1, 2]
        profits = [1, 2, 3]
        initial_capital = 1
        num_of_projects = 2

        self.assertEqual(6, two_heaps.maximize_capital(capitals, profits, initial_capital, num_of_projects))

        capitals = [0, 1, 2, 3]
        profits = [1, 2, 3, 5]
        initial_capital = 0
        num_of_projects =3

        self.assertEqual(8, two_heaps.maximize_capital(capitals, profits, initial_capital, num_of_projects))

    def test_next_interval(self):
        self.assertListEqual([1, 2, -1], two_heaps.next_interval([[2, 3], [3, 4], [5, 6]]))
        self.assertListEqual([2, -1, -1], two_heaps.next_interval([[3, 4], [1, 5], [4, 6]]))


if __name__ == '__main__':
    unittest.main()
