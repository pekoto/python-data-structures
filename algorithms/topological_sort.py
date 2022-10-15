from typing import List

import sys

sys.path.append('~/Documents/GitHub/python-data-structures/algorithms/python-data-structures/')

from data_structures.directed_graph_unweighted import DirectedGraphUnweighted


def topological_sort(graph: DirectedGraphUnweighted) -> List[str]:
    """A topological sort implemented using Kahn's algorithm.

    Kahn's algorithm can be used to topologically sort a graph,
    and to find loops in a graph so that it can't be topologically sorted.

    1. Store the in-degree of each vertex in a dict.
    2. Enqueue of the vertices with 0 in-degree.
    3. While the queue is not empty...
        * Pop a vertex and add it to the result
        * For each neighbor, decrease in-degree, and if it hits 0, enqueue it
    4. If the result does not include every vertex, there was a loop.
        (The vertex wouldn't have been added.)

    Time: O(V+E), loop round each vertex, and then each edge
    Space: O(V)
    """
    in_degree = {}

    # Gets in degree for each vertex
    for vertex in graph.vertices():
        if vertex not in in_degree:
            in_degree[vertex] = 0

        for neighbor in graph.neighbors_to(vertex):
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    # Get vertices with 0 in-degree
    queue = [vertex for vertex, count in in_degree.items() if count == 0]
    result = []

    while queue:
        vertex = queue.pop()
        result.append(vertex)

        for neighbor in graph.neighbors_to(vertex):
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph.vertices()):
        return None  # Graph had a loop

    return result
