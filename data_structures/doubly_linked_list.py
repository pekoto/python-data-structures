from typing import Any


class Node:

    def __init__(self, val: Any) -> None:
        self.val = val
        self.previous = None
        self.next = None

    def __str__(self):
        return self.val


class DoublyLinkedList:
    """A double linked list. Could also be a queue or deque (deck).

    deque = "deck", double-ended queue.

    Uses:
        * Implement stack or queue.
        * No need to resize.
        * Add left/right: O(1)
        * Pop left/right: O(1)
        * Remove: O(1)
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0

    def add_left(self, val: Any) -> None:
        """Adds a value to the left of the list.

        If the tail doesn't exist, set head=tail.
        Else, save the old head, and point the new and old heads to each other.

        Time: O(n)
        Space: O(n)

        :param val: The value to add.
        """
        old_head = self._head
        self._head = Node(val)

        if not self._tail:
            # Adding to empty list.
            self._tail = self._head
        else:
            self._head.next = old_head
            old_head.previous = self._head

        self.size += 1

    def add_right(self, val: Any) -> None:
        """Adds a value to the right of the list.

        If the head doesn't exist, set head=tail.
        Else, save the old tail, and point the new and old tails to each other.

        Time: O(n)
        Space: O(n)

        :param val: The value to add.
        """
        old_tail = self._tail
        self._tail = Node(val)

        if not self._head:
            # Adding to empty list.
            self._head = self._tail
        else:
            old_tail.next = self._tail
            self._tail.previous = old_tail

        self.size += 1

    def pop_left(self) -> Any:
        """Removes and returns the value at the left of the list.

        Time: O(n)
        Space: O(n)

        :return None
        """
        if not self._head:
            raise Exception('List is empty.')

        val = self._head.val
        self._head = self._head.next
        self.size -= 1

        if not self._head:
            # 1-element list.
            self._tail = None

        return val

    def pop_right(self) -> Any:
        """Removes and returns the value at the right of the list.

        Time: O(n)
        Space: O(n)

        :return None
        """
        if not self._tail:
            raise Exception('List is empty.')

        val = self._tail.val
        self._tail = self._tail.previous
        self.size -= 1

        if not self._tail:
            # 1-element list.
            self._head = None

        return val

    def remove_val(self, val: Any) -> None:
        """Removes the specified value from the list.

        Time: O(n)
        Space: O(1)

        :param val: The value to remove.
        """
        if not self._head:
            raise Exception('List is empty.')

        current_node = self._head

        while current_node and current_node.val != val:
            current_node = current_node.next

        if not current_node:
            raise KeyError(f'Key not found: {val}.')

        if current_node == self._head:
            self.pop_left()
        elif current_node == self._tail:
            self.pop_right()
        else:
            current_node.previous.next = current_node.next
            current_node.next.previous = current_node.previous
            self.size -= 1

    def reverse(self) -> None:
        """Reverses the list.

        1. Set up previous, current, and next
        2. Save the old head
        3. while current:
            * Save next node
            * Set current.next = prev, current.prev = next
            * Update prev = current, current = next
        4. Set tail = old head, head = prev

        * 1 > 2 > 3

        Time: O(n)
        Space: O(1)
        """
        if self.size <= 1:
            return

        previous = None
        current = self._head
        next_node = None

        old_head = self._head

        while current:
            next_node = current.next

            # Switch pointers.
            current.next = previous
            current.previous = next_node

            # Update nodes.
            previous = current
            current = next_node

        self._tail = old_head
        self._head = previous
