from collections import defaultdict
import heapq


def min_cost_connect_all_points(points: list[list[int]]) -> int:
    """
    Given an array of points on a 2D plane, give the minimum possible
    cost to connect all points.

    The minimum cost to connect points tells you this is an MST problem.

    To do this, we can use Prim's algorithm.
    Prim's algorithm is a greedy algorithm that lets us
    connect all nodes without a cycle, with minimum cost.

    1. Create an adjaceny list of edges with weights (distances)
    2. Start at any node in the graph
    3. Perform a BFS from that node, using a min heap to get next closest node.

    Time: O(n^2 log n) -- n^2 because we add each neighbor each time, log n for heap.
    Space: O(n^2) -- we could have all nodes in the min heap
    """
    num_points = len(points)

    graph = defaultdict(list)  # Each node has a list of ppints [cost, neighbor]

    # Build an adjacency list of points to distances and neighbors
    for i in range(num_points):
        x1, y1 = points[i]
        for j in range(i+1, num_points):
            x2, y2 = points[j]

            distance = abs(x1-x2) + abs(y1-y2)
            graph[i].append([distance, j])
            graph[j].append([distance, i])

    min_cost = 0
    visited = set()
    min_heap = []

    heapq.heappush(min_heap, (0, 0))  # Start at point 0, with cost 0

    while len(visited) < num_points:
        cost, next_closest = heapq.heappop(min_heap)
        if next_closest in visited:
            continue  # Already visited

        min_cost += cost
        visited.add(next_closest)

        for distance, neighbor in graph[next_closest]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (distance, neighbor))

    return min_cost

