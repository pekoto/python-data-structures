import unittest
import matrix_traversal


class MatrixTraversalTest(unittest.TestCase):

    def test_count_islands(self):
        matrix = [
            [1, 1, 1, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0],
        ]

        self.assertEqual(3, matrix_traversal.count_islands(matrix))

    def test_biggest_island(self):
        matrix = [
            [1, 1, 1, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ]

        self.assertEqual(5, matrix_traversal.biggest_island(matrix))

    def test_flood_fill(self):
        matrix = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ]

        expected_matrix = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 5, 5, 0],
            [0, 0, 5, 0, 0],
            [0, 0, 5, 0, 0],
        ]

        matrix_traversal.flood_fill(matrix, 3, 2, 5)

        self.assertListEqual(expected_matrix, matrix)

    def test_count_closed_islands(self):
        matrix = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        self.assertEqual(1, matrix_traversal.count_closed_islands(matrix))

    def test_island_perimeter(self):
        matrix = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]

        self.assertEqual(14, matrix_traversal.island_perimeter(matrix))

    def test_count_distinct_islands(self):
        matrix = [
            [1, 1, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 1, 0],
        ]

        self.assertEqual(2, matrix_traversal.count_distinct_islands(matrix))

    def test_matrix_cycle(self):
        matrix_1 = [['a', 'a', 'a', 'a'],
                    ['b', 'a', 'c', 'a'],
                    ['b', 'a', 'c', 'a'],
                    ['b', 'a', 'a', 'a']]

        matrix_2 = [['a', 'a', 'a', 'a'],
                    ['a', 'b', 'b', 'a'],
                    ['a', 'b', 'a', 'a'],
                    ['a', 'a', 'a', 'c']]

        matrix_3 = [['a', 'b', 'e', 'b'],
                    ['b', 'b', 'b', 'b'],
                    ['b', 'c', 'c', 'd'],
                    ['c', 'c', 'd', 'd']]

        self.assertTrue(matrix_traversal.matrix_cycle(matrix_1))
        self.assertTrue(matrix_traversal.matrix_cycle(matrix_2))
        self.assertFalse(matrix_traversal.matrix_cycle(matrix_3))


if __name__ == '__main__':
    unittest.main()
