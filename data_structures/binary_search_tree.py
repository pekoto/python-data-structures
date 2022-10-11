import sys
from typing import Any, List


class Node:
    """A class that represents a node in a Binary Search Tree."""

    def __init__(self, key: Any, val: Any, count: int) -> None:
        self.key = key
        self.val = val
        self.count = count

        self.left = None
        self.right = None


class BinarySearchTree:
    """A Binary Search Tree implementation.

    A tree with symmetric order:
        - Every element in the left subtree is < parent.
        - Every element in the right subtree is > parent.

    This means we can do binary searches since we know the direction
    to go (left or right) at each step.

    Operations typically take O(log n) time, but can take (n)
    time if values are inserted with a natural ordering (then we
    end up with a linked list).

    Uses:
        - Find k elements < value
        - Quick lookup/insert (if elements randomly ordered)
        - Print out min > max values (via inorder traversal)

    Operations:
        - Add
        - Get
        - Remove
        - Size
        - Max
        - Min
        _ Less than
        - Traversals
    """

    def __init__(self) -> None:
        """Initializes the Binary Search Tree."""
        self._root = None

    @property
    def root(self) -> Node:
        return self._root

    def add(self, key: Any, val: Any) -> None:
        """Adds a new node to the BST.

        1. If the node is empty, add it.
        2. If the node is < key, put it in left subtree.
        3. If the node is > key, put in the right subtree.
        4. If the  node is == key, just update the value.
        5. Update the count.
        6. Return the count.

                 2
                /  \
               1    3
        > add(0, 0)

                 2
                /  \
               1    3
              /
             0

        :param key: The key to add.
        :param val: The value to add.

        Time: O(log n) avg, O(n) worst.
        """
        self._root = self._add(self._root, key, val)

    def _add(self, node: Node, key: Any, val: Any) -> Node:
        """Helper method to add a new node."""
        if not node:
            return Node(key, val, 1)

        if key < node.key:
            node.left = self._add(node.left, key, val)
        elif key > node.key:
            node.right = self._add(node.right, key, val)
        else:
            node.val = val

        node.count = _size(node.left) + 1 + _size(node.right)

        return node

    def get(self, key: Any) -> Any:
        """Returns the value for a given key.

        1. Set the node to head.
        2. While node...
            - If key == node.key, return the val.
            - If key < node.key, search left.
            - If key > node.key, search right.

        Time: O(log n) avg, O(n) worst.

        :param key: The key to find in the BST.
        """
        node = self._root

        while node:
            if key == node.key:
                return node.val
            elif key < node.key:
                node = node.left
            else:
                node = node.right

        raise KeyError(f'Key not found: {key}')

    def remove(self, key: Any) -> None:
        """Removes a node from the binary search tree.

        This is the most complex operation, as we need to ensure
        the BST remains valid when removing a node.

        1. If the key is smaller, we remove in the left subtree.
        2. If the key is larger, we remove in the right subtree.
        3. Once we find the node to remove, things get tricky...

            - If the node has no right subtree, set node to left subtree,
                and vice-versa.

            Remove "1" (replaces with 1.5):
              2
             / \
            1   3
            \
             1.5
          (No left subtree, so right subtree must be next smallest)

            - If the node has left and right subtrees, replace with the smallest
                value in the right subtree.

             Remove "7" (replaces with 6)
                10
               / \
              7    12
             / \
            2   8
               /
              6
               \
               6.5

        Time:
            Average: O(n)
            Worst: O(sqrt(n))

        :param key: The key to remove.
        """
        self._root = self._remove(self._root, key)

    def _remove(self, node: Node, key: Any) -> Node:
        """Helper method to remove a node."""
        if not node:
            raise KeyError(f'Key not found: {key}.')

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                # Node has no left subtree -- set to right subtree.
                return node.right
            elif not node.right:
                # Node has no right subtree -- set to left subtree.
                return node.left
            else:
                # Node has left and right subtrees.
                node_to_delete = node

                # Replace the node with smallest node in right subtree.
                node = _min(node_to_delete.right)

                # Set right to be right subtree with smallest node removed.
                node.right = self._delete_min(node_to_delete.right)

                # Set left to be the left subtree.
                node.left = node_to_delete.left

        node.count = _size(node.left) + 1 + _size(node.right)
        return node

    def _delete_min(self, node: Node) -> Node:
        """Deletes the minimum node in a subtree.
        Once we hit a leftmost node, the min node will be that tree's right node.
        1. If the node in the left is null, return node.right.
        2. Delete from the left subtree.
        3. Update the count.
          7
         / \
        2   8
           /
          6
           \
           6.5
        :param node: The node to delete the min from.
        :return: The subtree with the minimum node deleted.
        """
        if not node.left:
            return node.right

        node.left = self._delete_min(node.left)
        node.count = _size(node.left) + 1 + _size(node.right)
        return node

    def size(self) -> int:
        """Returns the size of the tree."""
        return _size(self.root)

    def is_valid(self) -> bool:
        """Returns True if the BST is valid, or False otherwise.

        - Pass in the min and max bounds.
        - The node on the left must be between min and node key.
        - The node on the right must be between node key and max.
        """
        return self._is_valid(self._root, -sys.maxsize-1, sys.maxsize)

    def _is_valid(self, node: Node, min_bound: int, max_bound: int) -> bool:
        """Recursive helper function."""
        if not node:
            return True

        if node.key < min_bound or node.key > max_bound:
            return False

        return (self._is_valid(node.left, min_bound, node.key) and
                self._is_valid(node.right, node.key, max_bound))

    def inorder_traversal(self, nodes: List[Any]) -> None:
        """Inorder traversal.
           1. Traverse left
           2. Visit root
           3. Traverse right
           In a BST, gives nodes in ascending order.
                  5
               /    \
              3      8
             / \    / \
            1   4  7  10
           1, 3, 4, 5, 7, 8, 10
        """
        self._inorder_traversal(self._root, nodes)

    def _inorder_traversal(self, node: Node, nodes: List[Any]) -> None:
        """Recursive helper function."""
        if not node:
            return

        self._inorder_traversal(node.left, nodes)
        nodes.append(node.val)
        self._inorder_traversal(node.right, nodes)

    def preorder_traversal(self, nodes: List[Any]) -> None:
        """Preorder traversal.
        1. Visit root
        2. Traverse left
        3. Traverse right
        Can be used to create a copy of the tree.
               5
            /    \
           3      8
          / \    / \
         1   4  7  10
        5, 3, 1, 4, 8, 7, 10
        """
        self._preorder_traversal(self._root, nodes)

    def _preorder_traversal(self, node: Node, nodes: List[Any]) -> None:
        """Recursive helper function."""
        if not node:
            return

        nodes.append(node.val)
        self._preorder_traversal(node.left, nodes)
        self._preorder_traversal(node.right, nodes)

    def postorder_traversal(self, nodes: List[Any]) -> None:
        """Preorder traversal.
            1. Traverse left
            2. Traverse right
            3. Visit root
            Can be used to delete the tree.
                   5
                /    \
               3      8
              / \    / \
             1   4  7  10
            1, 4, 3, 7, 10, 8, 5
        """
        self._postorder_traversal(self._root, nodes)

    def _postorder_traversal(self, node: Node, nodes: List[Any]) -> None:
        """Recursive helper function."""
        if not node:
            return

        self._postorder_traversal(node.left, nodes)
        self._postorder_traversal(node.right, nodes)
        nodes.append(node.val)


def _size(node: Node) -> int:
    """Returns 0 if node is null, else returns size of node."""
    return 0 if not node else node.count


def _min(node: Node) -> Node:
    """Gets the minimum node from the tree"""
    if not node:
        raise Exception("Tried to get min on empty tree.")

    while node.left:
        node = node.left

    return node
