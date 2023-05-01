import unittest
from minimum_spanning_tree import min_cost_connect_all_points


class MyTestCase(unittest.TestCase):
    def test_min_cost_connect_all_points(self):
        self.assertEqual(20, min_cost_connect_all_points([[0, 0],[2, 2],[3, 10],[5, 2],[7, 0]]))


if __name__ == '__main__':
    unittest.main()
