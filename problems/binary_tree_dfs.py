from collections import deque
from typing import Any, List

from problems.fast_and_slow import Node


class TreeNode:

    def __init__(self, val: Any) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.next = None  # For "connect nodes" question only.

    def __str__(self) -> None:
        return self.val

    def __repr__(self) -> None:
        return repr(self.val)


def path_sum(root: TreeNode, target: int) -> bool:
    """
    Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf
    such that the sum of all the node values of that path equals ‘S’.

    Example: 10 --> True
         [1]
       2     [3]
     4  5  [6]  7
    """
    return _path_sum_dfs(root, 0, target)


def _path_sum_dfs(node: TreeNode, total: int, target: int) -> bool:
    """Recursive helper function."""
    if not node:
        return False

    new_total = total + node.val

    if new_total == target and not node.left and not node.right:
        return True

    return (_path_sum_dfs(node.left, new_total, target)
            or _path_sum_dfs(node.right, new_total, target))


def find_all_path_sums(root: TreeNode, target: int) -> List[List[int]]:
    """
    Given a binary tree and a number ‘S’, find all paths from root-to-leaf
    such that the sum of all the node values of each path equals ‘S’.

          1
       7     9
      4  5  2  7
    12 --> [1, 7, 4], [1, 9, 2]

    Time/Space discussion:
    If the tree is balanced, there will be log n from root to leaf.
    Given that we traverse each node once, and then copy the path from root to leave,
    we could say the time/space will be O(n log n).
    However, if it is not balanced, they will be O(n^2), since we might have a linked list.

    Similar problems:
    - Given a binary tree, return all root to leaf paths.
    - Given a binary tree, find the root to leaf path with a min/max sum.
    """
    result = []

    _find_all_path_sums_dfs(root, 0, target, result, [])

    return result


def _find_all_path_sums_dfs(
        node: TreeNode, sum_so_far: int, target: int, result: List[List[int]], path: List[int]) -> None:
    """Recursive helper function."""
    if not node:
        return

    new_sum = sum_so_far + node.val
    path.append(node.val)

    if new_sum == target and not node.left and not node.right:
        result.append(path.copy())

    _find_all_path_sums_dfs(node.left, new_sum, target, result, path)
    _find_all_path_sums_dfs(node.right, new_sum, target, result, path)

    path.pop()


def sum_of_path_numbers(root: TreeNode) -> int:
    """
    Given a binary tree where each node can only have a digit (0-9) value,
    each root-to-leaf path will represent a number.
    Find the total sum of all the numbers represented by all paths.

         1
       7   9
         2  9

    17 + 192 + 199 = 408
    """
    # (number so far * 10) + node.val
    # Can add all these to list and then sum them up
    # Can we improve space somehow? I think we can just do +=
    return _sum_of_path_numbers_dfs(root, 0)


def _sum_of_path_numbers_dfs(node: TreeNode, sum_so_far: int) -> int:
    """Recursive helper function."""
    if not node:
        return 0

    new_sum = (sum_so_far * 10) + node.val

    if not node.left and not node.right:
        return new_sum

    return (_sum_of_path_numbers_dfs(node.left, new_sum) +
            _sum_of_path_numbers_dfs(node.right, new_sum))


def count_paths_for_sum(root: TreeNode, target: int) -> int:
    """
    Given a binary tree and a number ‘S’, find all paths in the tree such
    that the sum of all the node values of each path equals ‘S’.
    Please note that the paths can start or end at any node but all paths
    must follow direction from parent to child (top to bottom).

         1
      7      9
    6   5  2   3

    12 --> 3 ([7, 5, 1], [9, 2], [9,3])

    Time: O(n^2), We traverse each node once, and at each node iterate the path,
                  which could we O(n) in the worst case.
    Space: O(n) for recursion stack.

    Note: The time can be improved to O(n) by storing a prefix sum array -- basically
          an map that stores the cumulative sum of any given path, and checking if the
          target or (current-target) number also exists in the map.
    """
    return _count_paths_dfs(root, target, [])


def _count_paths_dfs(node: TreeNode, target: int, path: List[int]) -> int:
    """Recursive helper function."""
    if not node:
        return 0

    path.append(node.val)
    path_count = 0

    # Find all sums of the all subpaths in the current path.
    # Note: We go BACKWARDS so we don't end up counting the same path
    # twice. We ONLY count paths ending at this node.
    path_sum = 0

    for i in range(len(path)-1, -1, -1):
        path_sum += path[i]

        if path_sum == target:
            path_count += 1

    path_count += _count_paths_dfs(node.left, target, path)
    path_count += _count_paths_dfs(node.right, target, path)

    path.pop()

    return path_count


def tree_diameter(root: TreeNode) -> int:
    """
    Given a binary tree, find the length of its diameter. The diameter of a
    tree is the number of nodes on the longest path between any two leaf
    nodes. The diameter of a tree may or may not pass through the root.

    Note: You can always assume that there are at least two leaf nodes in
    the given tree.

           1
        2    [3]
           [5]   [6]
        7  [8]   [9]
           [10] [11]
    Diameter = 7 [10, 8, 5, 3, 6, 9, 11]
    """
    result = [0]
    _tree_diameter_dfs(root, result)

    return result[0]


def _tree_diameter_dfs(node: TreeNode, result: List[int]) -> int:
    """Recursive helper function."""
    if not node:
        return 0

    left_height = _tree_diameter_dfs(node.left, result)
    right_height = _tree_diameter_dfs(node.right, result)

    node_diameter = left_height + 1 + right_height

    result[0] = max(result[0], node_diameter)

    return max(left_height, right_height) + 1


def max_path_sum(root: TreeNode) -> int:
    """
    Find the path with the maximum sum in a given binary tree. Write a function
    that returns the maximum sum.

    A path can be defined as a sequence of nodes between any two nodes and doesn’t
    necessarily pass through the root. The path must contain at least one node.

         [1]
      [2]   [3]
      [4]    5  [6]
    max_sum = 16
    """
    result = [0]
    _max_path_sum_dfs(root, result)

    return result[0]


def _max_path_sum_dfs(node: TreeNode, result: List[int]) -> int:
    """Recursive helper function."""
    if not node:
        return 0

    left_sum = _max_path_sum_dfs(node.left, result)
    right_sum = _max_path_sum_dfs(node.right, result)

    node_sum = left_sum + node.val + right_sum

    result[0] = max(result[0], node_sum)

    return max(left_sum, right_sum) + node.val


def get_height(root: TreeNode) -> int:
    """Finds the height of a BST.

            10
          /   \
         20   30
        /  \
      40   50

    """
    if not root:
        return 0

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    return max(left_height, right_height) + 1
