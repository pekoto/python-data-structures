from typing import Any

# Typically a power of two or prime number.
_ARRAY_SIZE = 97


class Node:
    """Represents a node in the hashmap."""

    def __init__(self, key: Any, val: Any, next_node) -> None:
        self.key = key
        self.val = val
        self.next = next_node


class HashMap:
    """A hashmap implemented with chaining.

    C.f. open addressing (used by Python). Open addressing is more memory
    efficient, but could end up have to readdress everything it the array requires resizing, since the hash
    algorithm requires the addresses to be of fixed size.
    Therefore, even though we may have more "wasted space", this behaves more
    gracefully as the array fills up.

    Operations:
    * Put(key, val): O(1) avg, O(n) worst [collisions]
    * Get(key): O(1) avg, O(n) worst
    * Remove(key): O(1) avg, O(n) worst
    * Contains(key): O(1) avg, O(n) worst
    """
    def __init__(self, size:int = _ARRAY_SIZE) -> None:
        """Initializes the hash map with a default size."""
        self._arr = [None] * size
        self.size = 0

    def put(self, key: Any, val: Any) -> None:
        """Adds a key and value to the hash map.

        1. Get the hash (array index)
        2. Get the node at that index
        3. While it's not null...
            If the key matches, update the val
            Else skip to next node
        4. Set the node at this index to be key, val, and next node

        Time: O(1) average, O(n) worst.
        """
        index = self._hash(key)
        node = self._arr[index]

        while node:
            if node.key == key:
                node.val = val
                return
            node = node.next

        self.size += 1
        self._arr[index] = Node(key, val, self._arr[index])

    def get(self, key: Any) -> Any:
        """Returns the value for this key."""
        index = self._hash(key)
        node = self._arr[index]

        while node:
            if node.key == key:
                return node.val
            node = node.next

        raise KeyError('Key not found!')

    def delete(self, key: Any) -> None:
        """Deletes a key from the hash map in a recursive fashion.
        1. Get the node at this index.
        2. Call the delete function with this node and key.
            2.1 If the node is null, raise a KeyError.
            2.2 If the node.key == key, return next node.
            2.3 Set node.next to a call with node.next
            2.4 Return the node.
        Time: O(1) average, O(n) worst case.
        """
        index = self._hash(key)
        self._arr[index] = self._delete(self._arr[index], key)

    def _delete(self, node: Node, key: Any) -> Node:
        """Delete helper method."""
        if not node:
            raise KeyError('Key not found!')

        if key == node.key:
            self.size -= 1
            return node.next

        node.next = self._delete(node.next, key)
        return node

    def _hash(self, key: Any) -> int:
        """Get the hash index to add an item to the map's array.

        * Take the abs value of the key's hash, then the modulus of the array size.
        """
        return abs(hash(key)) % len(self._arr)
