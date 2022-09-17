from typing import Any, List

_DEFAULT_RADIX_SIZE = 256


class Node:
    """Represents a node in the Trie.

    Each node contains len(radix) children.
    """
    def __init__(self, radix_size: int) -> None:
        self.val = None
        self.children = [None] * radix_size


class Trie:
    """A basic R-way Trie ("try"). Each node contains len(radix) children (i.e. R children).

    A node represents a character in the  radix, and has R children,
    representing the next character in the sequence. Strings are inserted one char at a time.

    The termination of a string is marked by an inserted value.

    So when searching, we just move down the tree until:
    - We hit a value (string terminated).
    - The char we are looking for does not exist as a child.

    Performance:
        Put: O(n)
        Search: O(n) [though typically less than this for misses, since we terminate early.]
                    Search performance can typically best a HashMap for strings.
        Memory:
            O(L*N*radix) -- num of strings * string len * radix size.
            This is a downsize, though it can be compressed.

        Uses:
            - Quick string matching
            - Spell checking
            - Prefix matching
                * Longest prefix O(n)
                * Keys with prefix O(n*radix_len)+O(l), where n is num of strings, and l is len of string.
    """
    def __init__(self, radix_size: int = _DEFAULT_RADIX_SIZE) -> None:
        self._radix_size = radix_size
        self._root = None

    def add(self, key: str, val: Any) -> None:
        """Adds key/val to the trie.

        1. If the node doesn't exist, instantiate it.
        2. If the index we're at is the length of the key, set value.
        3. Else, get the ASCII val of the char at this index.
        4. Set the child at this position to be the next char in the string.
        5. Return the node.

        Time: O(n)
        """
        self._root = self._add(self._root, key, val, 0)

    def _add(self, node: Node, key: str, val: Any, key_index: int) -> Node:
        """Recursive helper function."""
        if not node:
            node = Node(self._radix_size)

        # Reached the end of our key.
        if key_index == len(key):
            node.val = val
            return node

        # Add the next char in the key to the trie.
        # Think of it like stepping through our key string and
        # stepping down our trie at the same time.
        child_index = ord(key[key_index])
        node.children[child_index] = self._add(node.children[child_index], key, val, key_index+1)

        return node

    def get(self, key: str) -> Any:
        """Returns the value from the trie, or raises KeyError if not found.

        1. If the node is null, raise KeyError.
        2. If the key_index == the length of the key, we found it.
        3. Recurse with the next char in the key.
            (step through key, step down trie.)

        Time: O(n), where n is the length of the string.
            Although mismatches will typically have better performance.
        """
        node = self._get(self._root, key, 0)
        return node.val

    def _get(self, node: Node, key: str, key_index: int) -> Node:
        """Recursive helper function."""
        if not node:
            raise KeyError(f'Key not found: {key}')

        if key_index == len(key):
            # Finished searching.
            return node

        child_index = ord(key[key_index])

        return self._get(node.children[child_index], key, key_index+1)

