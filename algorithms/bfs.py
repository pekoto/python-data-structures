from collections import deque
from typing import Any, Dict, List


def bfs(graph: Dict[Any, List[Any]], source: Any) -> List[Any]:
    """A breadth-first search implementation.

    If we think of it like a tree, BFS visits one layer at a time.

    a-----b-----e
    | \   |     |
    |   \ |     |
    c-----d------

   bfs = [a, b, c, d, e]

    1. Set up visited, traversal, and queue (deque)
    2. Put the source in the queue
    3. Keep popping the queue, marking node as visited, and visiting neighbors.

    Can be modified to add distance, to get number of hops, distance from source to nodes etc.

    Time: O(V+E)
    Space: O(V)
    """
    visited = set()
    bfs_traversal = []
    queue = deque()

    # Appends the source onto the queue.
    queue.append(source)
    visited.add(source)

    while queue:
        # Count increment and set distance here
        current_node = queue.popleft()
        bfs_traversal.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_traversal
