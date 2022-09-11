from typing import Dict, List


class DirectedGraphWeighted:
    """A directed, weighted graph.

    To turn it into an undirected graph, we would just connect b to a in the connect method.
    (Undirected graph == digraph.)

    We could create a more nicely encapsulated "edge" class, but for quick implementation
    during interviews this is useful: we just create a dictionary for edges, where the key
    is the vertex id, and the value is the weight.

    Operations:
        add_vertex: O(1) average, O(n) worst case
        connect: O(1) average, O(n) worst case
        is_connected: O(1) average, O(n) worst case

    Space:
        O(V+E) = vertices + edges
    """

    def __init__(self) -> None:
        """Initializes the unweighted directed graph."""
        self._vertices = {}

    def add_vertex(self, vertex_id: str) -> None:
        """Adds or reinitializes a vertex.

        Time: O(1) avg, O(n) worst.

        param vertex_id: The vertex to add.
        """
        self._vertices[vertex_id] = {}

    def connect(self, vertex_a: str, vertex_b: str, weight: float) -> None:
        """Connects vertex a to b with given weight.

        Time: O(1) avg, O(n) worst.

        :param vertex_a: The vertex to connect from.
        :param vertex_b: The vertex to connect to.
        :param weight: The weight of the connection between the two vertices.
        """
        if vertex_a not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_a}.')

        if vertex_b not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_b}.')

        self._vertices[vertex_a][vertex_b] = weight
        # To make an undirected graph, we just connect back the other way.

    def is_connected(self, vertex_a: str, vertex_b: str) -> bool:
        """Returns True if vertex a is connected to vertex b directionally.
        Time: O(1) average, O(n) worst case
        :param vertex_a: The starting vertex.
        :param vertex_b: The vertex connected to.
        :return: True if vertex a is connected to vertex b, False otherwise.
        """
        if vertex_a not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_a}')

        if vertex_b not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_b}')

        return vertex_b in self._vertices[vertex_a]

    def weight(self, vertex_a: str, vertex_b: str) -> float:
        """Returns the weight if vertex a is connected to vertex b directionally.
        Time: O(1) average, O(n) worst case
        :param vertex_a: The starting vertex.
        :param vertex_b: The vertex connected to.
        :return: The weight of the connect between vertices a and b.
        """
        if vertex_a not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_a}')

        if vertex_b not in self._vertices:
            raise KeyError(f'Vertex not found: {vertex_b}')

        if vertex_b not in self._vertices[vertex_a]:
            raise Exception(f'{vertex_a} not connected to {vertex_b}')

        return self._vertices[vertex_a][vertex_b]

    def vertices(self) -> List[str]:
        """Returns the list of vertices in the graph."""
        return list(self._vertices.keys())

    def neighbours_to(self, vertex: str) -> Dict[str, float]:
        """Returns the neighbours for a given vertex.
        :param vertex: The vertex whose neighbours we want to find.
        :return: The neighbours
        """
        return self._vertices[vertex]
