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


def level_order_traversal(root: TreeNode) -> List[List[Any]]:
    """
    Given a binary tree, populate an array to represent its level-by-level
    traversal. You should populate the values of all nodes of each level
    from left to right in separate sub-arrays.

    [[1],
    [2, 3],
    [4,5,6,7]
    """
    queue = deque()
    queue.append(root)

    result = []

    while queue:

        level = []

        # Iterate around the previous level
        for _ in range(len(queue)):
            next_node = queue.popleft()
            level.append(next_node.val)

            if next_node.left:
                queue.append(next_node.left)

            if next_node.right:
                queue.append(next_node.right)

        result.append(level)

    return result


def reverse_level_order_traversal(root: TreeNode) -> List[List[Any]]:
    """
    Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
    i.e., the lowest level comes first. You should populate the values of all nodes in each level from
    left to right in separate sub-arrays.

    [[4, 5, 6, 7],
    [2, 3],
    [1]]
    """
    queue = deque()
    result = deque()
    queue.append(root)

    while queue:

        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.appendleft(level)

    return list(result)


def zigzag_traversal(root: TreeNode) -> List[List[Any]]:
    """
    Given a binary tree, populate an array to represent its zigzag level
    order traversal. You should populate the values of all nodes of the
    first level from left to right, then right to left for the next level
    and keep alternating in the same manner for the following levels.

    [[1],
    [3, 2],
    [4, 5, 6, 7]]
    """
    result = []
    queue = deque()
    queue.append(root)
    left_to_right = True

    while queue:

        level = deque()

        for _ in range(len(queue)):
            node = queue.popleft()

            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level))
        left_to_right = not left_to_right

    return result


def level_averages(root: TreeNode) -> List[float]:
    """
    Given a binary tree, populate an array to represent the averages of
    all of its levels.
    [1, 2.5, 5.5]

    Similar problem:
    Problem 1: Find the largest value on each level of a binary tree.
    """
    queue = deque()
    result = []

    queue.append(root)

    while queue:

        level_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / level_size)

    return result


def minimum_depth(root: TreeNode) -> int:
    """
    Find the minimum depth of a binary tree.
    The minimum depth is the number of nodes along the
    shortest path from the root node to the nearest leaf node.

    Similar problem: Find the maximum depth.
    """
    min_depth = 0

    queue = deque()
    queue.append(root)

    while queue:
        min_depth += 1

        for _ in range(len(queue)):
            node = queue.popleft()

            if not node.left and not node.right:
                return min_depth

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return min_depth


def level_order_successor(root: TreeNode, node_key: int) -> int:
    """
    Given a binary tree and a node, find the level order successor of
    the given node in the tree. The level order successor is the node
    that appears right after the given node in the level order traversal.

             1
           2   3
         4   5
    Given 3 > return 4
    """
    queue = deque()
    queue.append(root)
    key_found = False

    while queue:

        for _ in range(len(queue)):

            node = queue.popleft()

            if key_found:
                return node.val

            if node.val == node_key:
                key_found = True

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return -1


def connect_level_order_siblings(root: TreeNode) -> None:
    """
    Given a binary tree, connect each node with its level order successor.
    The last node of each level should point to a null node.

          1 > None
      2   >   3 > None
    4 > 5 > 6 > 7 > None
    """
    queue = deque()
    queue.append(root)

    while queue:

        node = None
        previous_node = None

        for _ in range(len(queue)):

            if node:
                previous_node = node

            node = queue.popleft()

            if node and previous_node:
                previous_node.next = node

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


def connect_all_level_order_siblings(root: TreeNode) -> None:
    """
    Given a binary tree, connect each node with its level order successor.
    The last node of each level should point to the first node of the next level.

           1 >
      2 >     3 >
    4 > 5 > 6 > 7 > None
    """
    queue = deque()
    queue.append(root)
    previous_level_tail = None
    node = None
    previous_node = None

    while queue:

        level_size = len(queue)

        for i in range(level_size):

            if node:
                previous_node = node

            node = queue.popleft()

            if previous_node:
                # At the start of the level, connect the previous level's tail.
                previous_node.next = node

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


def right_view(root: TreeNode) -> List[int]:
    """
    Given a binary tree, return an array containing nodes in its right view.
    The right view of a binary tree is the set of nodes visible when the tree
    is seen from the right side.

            [1]
         2      [3]
      4    5  6     [7]
    """
    result = []
    queue = deque()
    queue.append(root)

    while queue:

        queue_len = len(queue)

        for i in range(queue_len):

            node = queue.popleft()

            if i == queue_len-1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return result
