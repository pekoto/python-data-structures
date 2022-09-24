import unittest
from dfs import dfs


class DfsTest(unittest.TestCase):

    def test_dfs(self):
        graph = {
            'a': ['b', 'c'],
            'b': ['d'],
            'c': ['d'],
            'd': ['e'],
            'e': [],
        }

        expected_dfs_traversal = ['a', 'b', 'd', 'e', 'c']

        actual_dfs_traversal = dfs(graph, 'a')

        self.assertListEqual(expected_dfs_traversal, actual_dfs_traversal)


if __name__ == '__main__':
    unittest.main()
