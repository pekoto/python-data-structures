from typing import Any


class Node:

    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None

    def __str__(self) -> None:
        return self.val


class LinkedList:
    """A single linked list.

    Add: O(n)
    Remove: O(n)
    Lookup: O(n)

    Uses:
    * Implement stacks or queues
    * Adjacency list representation of graphs
    * Chained hashmap chains
    * No need to resize when growing or shrinking
      (generally a double-linked list will give better performance though)
    """

    def __init__(self) -> None:
        self._head = None
        self.size = 0

    def add_recursive(self, val: Any) -> None:
        """Adds a new item to the linked list in a recursive manner.

        If the node is null, set initialize a new node and return it.
        Else, recurse through the list until we hit a null node, initialize
        a node, and set this node to be the previous node's next node.

        Example:
        1 > 2 > add_recursive(3)

        - add_recursive(1, 3)
        - 1.next = add_recursive(2, 3)
        - 2. next = add_recursive(3, null)
        - 2.next = 3

        Time: O(n)
        Space: O(n) -- due to callstack growth.

        :param val: The value to add.
        :return: None
        """
        self._head = self._add_recursive(self._head, val)
        self.size += 1

    def _add_recursive(self, node: Node, val: Any) -> Node:
        """Adds a node recursively."""
        if not node:
            return Node(val)

        node.next = self._add_recursive(node.next, val)
        return node

    def add_iterative(self, val: Any) -> None:
        """Adds a new node in an iteratively.

        Time: O(n)
        Space: O(1)

        :param val: The value to add.
        :return: None
        """
        if not self._head:
            self._head = Node(val)
        else:
            node = self._head
            while node.next:
                node = node.next
            node.next = Node(val)

        self.size += 1

    def remove_recursive(self, val: Any) -> None:
        """Removes a node recursively.

        If the node is not found, raise a KeyError.
        Elif, if the val is found, return node.next.
        Else, recurse with node.next.

        Example:
        1 > 2 > 3, remove_recursive(2)

        - _remove_recursive(1, 2)
        - 1.next = _remove_recursive(2, 2)
        - 1.next = 2.next = 3

        Time: O(n)
        Space: O(n) -- due to call stack growth.

        :param val: The value to remove.
        :return: None
        """
        self._remove_recursive(self._head, val)

    def _remove_recursive(self, node: Node, val: Any) -> Node:
        if not node:
            raise KeyError(f'Key not found: {val}')

        if node.val == val:
            self.size -= 1
            return node.next

        node.next = self._remove_recursive(node.next, val)

    def remove_iterative(self, val: Any) -> None:
        """Removes a node iteratively.

        If the head is null, raise a KeyError.

        If the head matches, simply set head = head.next.
        Else, loop around until the next value matches out key.
        Then set next to be next.next.

        Ex. 1 > 2 > 3, remove_iterative(2)

        node = 1
        node.next = 2
        1.next = 2.next = 3

        Time: O(n)
        Space: O(1)

        :param val: The value to remove.
        :return: None.
        """
        if not self._head:
            raise KeyError(f'Key not found: {val}')

        if self._head.val == val:
            self._head = self._head.next
            self.size -= 1
        else:
            node = self._head

            while node.next and node.next.val != val:
                node = node.next

            if not node.next:
                raise KeyError(f'Key not found: {val}')

            node.next = node.next.next
            self.size -= 1

    def reverse(self) -> None:
        """Reverses the linked list.

        1 > 2 > 3

        1. Set up previous, current, and next.
        2. While current:
            next = current.next        # Save next
            current.next = previous    # Set next to last node
            previous = current         # Save current node, previous
            current = next             # Move to next node
        3. Set the head to be previous.

        Time: O(n)
        Space: O(1)

        :return: None
        """
        if not self._head or not self._head.next:
            return

        previous = None
        current = self._head
        next_node = None

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self._head = previous

    def is_empty(self) -> bool:
        return self.size == 0
