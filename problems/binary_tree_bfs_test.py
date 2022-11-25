import unittest

from problems import binary_tree_bfs
from problems.binary_tree_bfs import TreeNode


class BinaryTreeBfsTest(unittest.TestCase):

    def test_level_order_traversal(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        expected_list = [[1], [2, 3], [4, 5, 6, 7]]

        self.assertListEqual(expected_list, binary_tree_bfs.level_order_traversal(root))

    def test_reverse_level_order_traversal(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        expected_list = [[4, 5, 6, 7], [2, 3], [1]]

        self.assertListEqual(expected_list, binary_tree_bfs.reverse_level_order_traversal(root))

    def test_zigzag_traversal(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        expected_list = [[1], [3, 2], [4, 5, 6, 7]]

        self.assertListEqual(expected_list, binary_tree_bfs.zigzag_traversal(root))

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        root.right.left.left = TreeNode(20)
        root.right.left.right = TreeNode(17)

        expected_list = [[12], [1, 7], [9, 10, 5], [17, 20]]

        self.assertListEqual(expected_list, binary_tree_bfs.zigzag_traversal(root))

    def test_level_averages(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        expected_list = [1, 2.5, 5.5]

        self.assertListEqual(expected_list, binary_tree_bfs.level_averages(root))

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        expected_list = [12, 4, 6.5]

        self.assertListEqual(expected_list, binary_tree_bfs.level_averages(root))

    def test_minimum_depth(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        self.assertEqual(2, binary_tree_bfs.minimum_depth(root))

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        self.assertEqual(2, binary_tree_bfs.minimum_depth(root))

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        root.right.left.left = TreeNode(11)

        self.assertEqual(3, binary_tree_bfs.minimum_depth(root))

    def test_level_order_successor(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        self.assertEqual(4, binary_tree_bfs.level_order_successor(root, 3))

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        self.assertEqual(10, binary_tree_bfs.level_order_successor(root, 9))

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        self.assertEqual(7, binary_tree_bfs.level_order_successor(root, 12))

    def test_connect_level_order_siblings(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        binary_tree_bfs.connect_level_order_siblings(root)

        self.assertIsNone(root.next)
        self.assertEqual(root.left.next, root.right)
        self.assertEqual(root.left.left.next, root.left.right)
        self.assertEqual(root.left.left.next.next, root.right.left)
        self.assertEqual(root.left.left.next.next.next, root.right.right)

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        binary_tree_bfs.connect_level_order_siblings(root)

        self.assertIsNone(root.next)
        self.assertEqual(root.left.next, root.right)
        self.assertEqual(root.left.left.next, root.right.left)
        self.assertEqual(root.left.left.next.next, root.right.right)

    def test_connect_all_level_order_siblings(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        binary_tree_bfs.connect_all_level_order_siblings(root)

        self.assertEqual(root.next, root.left)
        self.assertEqual(root.left.next, root.right)
        self.assertEqual(root.right.next, root.left.left)
        self.assertEqual(root.left.left.next, root.left.right)
        self.assertEqual(root.left.right.next, root.right.left)
        self.assertEqual(root.right.left.next, root.right.right)
        self.assertIsNone(root.right.right.next)

    def test_right_view(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        self.assertListEqual([1, 3, 7], binary_tree_bfs.right_view(root))

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        root.left.left.left = TreeNode(3)

        self.assertListEqual([12, 1, 5, 3], binary_tree_bfs.right_view(root))


if __name__ == '__main__':
    unittest.main()
