from typing import Any, Dict, List, Set


def dfs(graph: Dict[Any, List[Any]], source: Any) -> List[Any]:
    """A depth-first search implementation.

    A recursive traversal algorithm. If we think of the graph like a tree,
    a depth-first search goes down to the root and then comes back up.

    a-----b
    | \   |
    |  \  |
    c-----d-----e

    dfs_traversal = [a, b, d, e, c]

    Uses:
    * Detect cycle in the graph
    * Path finding
    * Topological sorting
    * Find strongly connected components (islands)

    Time: O(v+e)
    Space: O(v)
    """
    dfs_traversal = []
    visited = set()

    _dfs(graph, source, dfs_traversal, visited)

    return dfs_traversal


def _dfs(graph: Dict[Any, List[Any]], vertex: Any, dfs_traversal: List[Any], visited: Set[Any]) -> None:
    """Recursive helper function."""
    if vertex in visited:
        return

    visited.add(vertex)
    dfs_traversal.append(vertex)

    for neighbor in graph[vertex]:
        _dfs(graph, neighbor, dfs_traversal, visited)
