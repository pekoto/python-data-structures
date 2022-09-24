import unittest

from bfs import bfs


class BfsTest(unittest.TestCase):

    def test_bfs(self):
        graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd', 'e'],
            'c': ['a', 'd'],
            'd': ['b', 'c', 'a', 'e'],
            'e': ['b', 'd'],
        }

        expected_bfs_traversal = ['a', 'b', 'c', 'd', 'e']

        actual_bfs_traversal = bfs(graph, 'a')

        self.assertListEqual(expected_bfs_traversal, actual_bfs_traversal)


if __name__ == '__main__':
    unittest.main()
