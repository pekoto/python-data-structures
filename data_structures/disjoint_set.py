from typing import List


class DisjointSet:
    """A Disjoint Set / Union-Find data structure.

    This can be used for things such as:
        1. Finding number of connected components
        2. Finding if 2 components are connected and so on.

    Two operations:
    - Find: Find if parents are connected. O(n), <O(log n) if optimized with path compression/weighting.
    - Union: Join 2 components together. Also O(n), <O(log n) if optimized with path compression and weighting.
    """

    def __init__(self, vertices: List[int]) -> None:
        """Initializes the union-find structure."""
        self._vertices = vertices
        self._parents = {}

        for vertex in self._vertices:
            self._parents[vertex] = vertex

    def union(self, vertex_a: int, vertex_b: int) -> None:
        """Unions two vertices together.

        - Find the parent of vertex a
        - Find the parent of vertex b
        - Make the parent of vertex a = parent of vertex b

        p: 1  2  1  4  5
        v: 1, 2, 3, 4, 5

        > union(3, 5)

        p: 5* 2  1  4  5
        v: 1, 2, 3, 4, 5

        Time: O(n)
        """
        vertex_a_parent = self.find(vertex_a)
        vertex_b_parent = self.find(vertex_b)

        self._parents[vertex_a_parent] = vertex_b_parent

    def find(self, vertex: int) -> int:
        """Finds the parent of a given vertex.

        - If the parent is itself, return it
        - Otherwise, call recursive on the parent (find parent's parent)
        - Set the parent of that vertex to be the parent (optional: path compression)

        Time: O(n), but < O(log n) with path compression & weighting (not implemented)
        """
        if self._parents[vertex] == vertex:
            return vertex
        else:
            parent = self.find(self._parents[vertex])
            self._parents[vertex] = parent  # Path compression
            return parent

    def are_connected(self, vertex_a, vertex_b) -> bool:
        """Returns True if two vertices are connected."""
        return self.find(vertex_a) == self.find(vertex_b)
