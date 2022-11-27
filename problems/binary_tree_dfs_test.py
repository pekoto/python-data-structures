import unittest
from problems import binary_tree_dfs
from problems.binary_tree_dfs import TreeNode


class BinaryTreeDfs(unittest.TestCase):

    def test_path_sum(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        self.assertTrue(binary_tree_dfs.path_sum(root, 10))

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.left.left = TreeNode(9)
        root.right = TreeNode(1)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        self.assertTrue(binary_tree_dfs.path_sum(root, 23))
        self.assertFalse(binary_tree_dfs.path_sum(root, 16))

    def test_final_all_path_sums(self):
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(9)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(7)

        self.assertListEqual([[1, 7, 4], [1, 9, 2]], binary_tree_dfs.find_all_path_sums(root, 12))

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.left.left = TreeNode(4)
        root.right = TreeNode(1)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        self.assertListEqual([[12, 7, 4], [12, 1, 10]], binary_tree_dfs.find_all_path_sums(root, 23))

    def test_sum_of_path_numbers(self):
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(9)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(9)

        self.assertEqual(408, binary_tree_dfs.sum_of_path_numbers(root))

        root = TreeNode(1)
        root.left = TreeNode(0)
        root.left.left = TreeNode(1)
        root.right = TreeNode(1)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(5)

        self.assertEqual(332, binary_tree_dfs.sum_of_path_numbers(root))

    def test_count_paths_for_sum(self):
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(9)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(3)

        self.assertEqual(3, binary_tree_dfs.count_paths_for_sum(root, 12))

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        self.assertEqual(2, binary_tree_dfs.count_paths_for_sum(root, 11))

    def test_tree_diameter(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)

        self.assertEqual(5, binary_tree_dfs.tree_diameter(root))

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.left.left = TreeNode(7)
        root.right.left.right = TreeNode(8)
        root.right.left.right.left = TreeNode(10)
        root.right.right = TreeNode(6)
        root.right.right.left = TreeNode(9)
        root.right.right.left.left = TreeNode(11)

        self.assertEqual(7, binary_tree_dfs.tree_diameter(root))

    def test_max_path_sum(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)

        self.assertEqual(16, binary_tree_dfs.max_path_sum(root))

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.left.left = TreeNode(7)
        root.right.left.right = TreeNode(8)
        root.right.right = TreeNode(6)
        root.right.right.left = TreeNode(9)

        self.assertEqual(31, binary_tree_dfs.max_path_sum(root))


if __name__ == '__main__':
    unittest.main()
