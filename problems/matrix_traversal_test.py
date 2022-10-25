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

    def test_flood_fille(self):
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


if __name__ == '__main__':
    unittest.main()
