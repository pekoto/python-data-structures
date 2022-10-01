import unittest
from count_islands import count_islands


class CountIslandsTest(unittest.TestCase):

    def test_count_islands(self):
        land = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
        ]

        num_islands = count_islands(land)

        self.assertEqual(3, num_islands)


if __name__ == '__main__':
    unittest.main()
