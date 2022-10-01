import sys
from collections import deque
from queue import PriorityQueue
from typing import List

sys.path.append('~/Documents/GitHub/python-data-structures/algorithms/python-data-structures/')

from data_structures.directed_graph_weighted import DirectedGraphWeighted


class DijkstrasAlgorithm:
    """ Dijkstra's Algorithm finds the shortest path from a given vertex to
            all over vertices.

        1. Set the distance to all vertices to sys.maxsize
        2. Set the distance to source = 0, and put it in a PQ
        3. While the PQ isn't empty...
            3.1 Pop the closest vertex
            3.2 For each neighbour...
                3.2.1 If not visited, relax it
                3.2.2 Mark is as visited
        The relax process:
        1. The distance is the distance to the from vertex + weight
        2. If the current distance to this vertex > this distance...
            2.1 Set the new distance to be this
            2.2 Set the edge to be this from vertex
            2.3 Put this distance in the PQ
        Time: 0([V + E]*log(V) ) --  log V for putting vertices in PQ
                                      and V + E because we will visited each vertex + edge.
        Space: O(V)
        Uses:
            - Map applications
            - Shortest paths
    """

    def __init__(self, graph: DirectedGraphWeighted, starting_vertex: str) -> None:
        self._edge_to = {}
        self._distance_to = {}
        self._visited = set()
        self._pq = PriorityQueue()
        self._starting_vertex = starting_vertex

        for vertex in graph.vertices():
            self._distance_to[vertex] = sys.maxsize

        self._distance_to[starting_vertex] = 0

        self._pq.put((0, starting_vertex))

        while not self._pq.empty():
            current_vertex = self._pq.get()[1]

            for neighbor, weight in graph.neighbours_to(current_vertex).items():
                if neighbor not in self._visited:
                    self._relax(current_vertex, neighbor, weight)

            self._visited.add(current_vertex)

    def _relax(self, from_vertex: str, to_vertex: str, weight: float) -> None:
        """Runs the relax process.

        1. The distance to this vertex is the distance to the from vertex + weight
        2. If this is shorter than current distance...
            * Set the new distance to be this distance
            * Set the edge to to be the from vertex
            * Put this distance in the PQ
        """
        distance_along_this_path = self._distance_to[from_vertex] + weight

        if self._distance_to[to_vertex] > distance_along_this_path:
            self._distance_to[to_vertex] = distance_along_this_path
            self._edge_to[to_vertex] = from_vertex

            # For -ve weights, we could remove the node from the pq if it
            # already exists (or mark it as processed), and then not check if
            # a neighbour has been visited.

            self._pq.put((distance_along_this_path, to_vertex))

    def distance_to(self, destination_vertex: str) -> float:
        """Returns the distance to the destination vertex."""
        return self._distance_to[destination_vertex]

    def path_to(self, destination_vertex: str) -> List[str]:
        """Gets the path to the destination vertex."""
        path = deque()

        path.append(destination_vertex)
        vertex = self._edge_to[destination_vertex]

        while vertex != self._starting_vertex:
            path.appendleft(vertex)
            vertex = self._edge_to[vertex]

        path.appendleft(vertex)

        return list(path)
