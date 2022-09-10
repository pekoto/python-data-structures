from typing import List


class DirectedGraphUnweighted:
    """A directed graph implementation using an adjaceny list.

    (Actually we can use a set instead of a list to improve performance.)

    To turn this into an undirected graph, we just connect b to a as well as a to b.
    Example:

    | Vertex | Edges |
    ------------------
    |  0    | [1, 2]
    |  1    | []
    |  2    | [4]
    |  3    | [0]

    3 -->  0 --> 1
           |
           2 --> 4

    An alternative approach it to use an adjacency matrix, where 1 represents an edge.

    Operations:
        - add_vertex: O(1) avg, O(n) worst
        - connect: O(1) avg, O(n) worst
        - is_connected: O(1) avg, O(n) worst

    Space:
        O(V+E) + vertices + edges
    """
    def __init__(self) -> None:
        """Initializes the directed graph."""
        self._vertices = {}

    def add_vertex(self, vertex_id: str) -> None:
        """Adds or reinitializes a vertex in the graph.

        Time: O(1) avg, O(n) worst.
        :param vertex_id: The ID of the vertex to add.
        """
        self._vertices[vertex_id] = set()

    def connect(self, vertex_a: str, vertex_b: str) -> None:
        """Connects to vertices in the graph.

        Time: O(1) avg, O(n) worst.

        :param vertex_a: The vertex to connect from.
        :param vertex_b: The vertex to connect to.
        """
        if vertex_a not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_a}')

        if vertex_b not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_b}')

        self._vertices[vertex_a].add(vertex_b)
        # To make an undirected graph, we would just connect vertex_b to vertex_a here.

    def is_connected(self, vertex_a: str, vertex_b: str) -> bool:
        """Returns True if vertex_a is connected to vertex_b.

        Time: O(1) avg, O(n) worst case.

        :param vertex_a: The starting vertex.
        :param vertex_b: The vertex connected to.
        :return: True if vertex a is connected to vertex b, False otherwise.
        """
        if vertex_a not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_a}')

        if vertex_b not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_b}')

        return vertex_b in self._vertices[vertex_a]

    def vertices(self) -> List[str]:
        """Returns the list of vertices in the graph."""
        return list(self._vertices.keys())

    def neighbors_to(self, vertex_id: str) -> List[str]:
        """Returns the neighbours to a given vertex."""
        return list(self._vertices[vertex_id])
