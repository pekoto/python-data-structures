import unittest

from disjoint_set import DisjointSet


class DisjointSetTest(unittest.TestCase):

    def test_union_find(self):
        vertices = [1, 2, 3, 4, 5]

        disjoint_set = DisjointSet(vertices)

        disjoint_set.union(1, 3)
        disjoint_set.union(3, 5)

        self.assertTrue(disjoint_set.are_connected(1, 3))
        self.assertTrue(disjoint_set.are_connected(3, 5))
        self.assertTrue(disjoint_set.are_connected(1, 5))
        self.assertFalse(disjoint_set.are_connected(1, 2))
        self.assertFalse(disjoint_set.are_connected(4, 3))


if __name__ == '__main__':
    unittest.main()
