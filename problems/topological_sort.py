from collections import deque


def topological_sort(edges: list[list[int]]) -> list[int]:
    """
    Given a directed graph, find the topological ordering of its vertices.

    [3, 2], [3, 0], [2, 0], [2, 1] -> 3, 2, 0, 1 or 3, 2, 1, 0

    3 -> 2 -> 1
    |    |
    -------->0

    Time: O(V+E) -- Each vertex becomes source, and each edge accessed and removed once.
    Space: O(V+E) -- Store each vertex for each vertex in the adjacency list.
    """
    in_degree = {}
    neighbors = {}

    # Get the in-degree for each vertex, and build a list of neighbors.
    for edge in edges:
        if edge[0] not in in_degree:
            in_degree[edge[0]] = 0

        if edge[1] not in in_degree:
            in_degree[edge[1]] = 0

        if edge[0] not in neighbors:
            neighbors[edge[0]] = []

        if edge[1] not in neighbors:
            neighbors[edge[1]] = []

        in_degree[edge[1]] += 1
        neighbors[edge[0]].append(edge[1])

    queue = deque()

    # Start with vertices that have in-degree == 0.
    for vertex, count in in_degree.items():
        if count == 0:
            queue.append(vertex)

    result = []

    # Pop the queue to get the next vertex.
    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        # Decrement the in-degree of all of the neighbors.
        for neighbor in neighbors[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(in_degree.keys()) != len(result):
        return [-1]  # Graph had a loop

    return result


def can_schedule(prerequisites: list[list[int]]) -> bool:
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some
    prerequisite tasks which need to be completed before it can be scheduled.
    Given the number of tasks and a list of prerequisite pairs, find out if it is
    possible to schedule all the tasks.

    [0, 1], [1, 2] -> True (0, 1, 2)
    [0, 1], [1, 2], [2, 0] -> False (loop from 2>0)
    """
    in_degree = {}
    neighbors = {}

    for prerequisite in prerequisites:
        if prerequisite[0] not in in_degree:
            in_degree[prerequisite[0]] = 0

        if prerequisite[1] not in in_degree:
            in_degree[prerequisite[1]] = 0

        if prerequisite[0] not in neighbors:
            neighbors[prerequisite[0]] = []

        if prerequisite[1] not in neighbors:
            neighbors[prerequisite[1]] = []

        neighbors[prerequisite[0]].append(prerequisite[1])
        in_degree[prerequisite[1]] += 1

    queue = deque()

    for vertex, count in in_degree.items():
        if count == 0:
            queue.append(vertex)

    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in neighbors[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return len(result) == len(in_degree.keys())


def task_schedule(prerequisites: list[list[int]]) -> list[int]:
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
    Each task can have some prerequisite tasks which need to be completed
    before it can be scheduled. Given the number of tasks and a list of
    prerequisite pairs, write a method to find the ordering of tasks we should
    pick to finish all tasks.

    [0, 1], [1, 2] -> [0, 1, 2]
    """
    in_degree = {}
    neighbors = {}

    for prerequisite in prerequisites:
        if prerequisite[0] not in in_degree:
            in_degree[prerequisite[0]] = 0

        if prerequisite[1] not in in_degree:
            in_degree[prerequisite[1]] = 0

        if prerequisite[0] not in neighbors:
            neighbors[prerequisite[0]] = []

        if prerequisite[1] not in neighbors:
            neighbors[prerequisite[1]] = []

        in_degree[prerequisite[1]] += 1
        neighbors[prerequisite[0]].append(prerequisite[1])

    queue = deque()

    for vertex, count in in_degree.items():
        if count == 0:
            queue.append(vertex)

    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in neighbors[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(in_degree.keys()):
        return []

    return result


def all_task_schedules(prerequisites: list[list[int]]) -> list[list[int]]:
    """
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some
    prerequisite tasks which need to be completed before it can be scheduled.
    Given the number of tasks and a list of prerequisite pairs, write a method
    to print all possible ordering of tasks meeting all prerequisites.

    [3, 2], [3, 0], [2, 0], [2, 1] -> [3, 2, 0, 1], [3, 2, 1, 0]

    3 -> 2 ->  1   0
    |----|---------^
    """
    # Solution:
    # For each vertex in the queue (of sources) we're going to process it by:
    # 1. Copying the queue
    # 2. Removing the vertex we want to process
    # 3. Get the next neighbors to process
    # 4. Call recursively
    # 5. Check if our queue is empty and result has all vertices (found a result)
    # 6. Backtrack: Remove vertex from the result and increment all the neighbors
    #       (Since we removed the vertex from a queue copy, not the original queue, don't need to put it back there)
    #
    # Example:
    # In_degree: {3: 0, 2: 1, 1: 1, 0: 2}
    # Neighbors: {3: [2, 0], 2: [0, 1], 1: [], 0: []}
    # 1. Our queue is 3, add 3 to result, next is [2]
    # 2. Our queue is 2, add 2 to result, next is [0, 1]
    # 3. Now, we remove 0 to the queue copy, 1 is left in the queue
    # 4. We add 1 to the result, the queue is empty, so we have our first result [3, 2, 0, 1]
    # 5. Now backtrack to 3). We increment neighbors for 0, remove it from the result, [3, 2, 1]
    # 6. So now 0 is in the queue again...etc.
    # Time: Since we have n! permutations, we have O(v!*e)
    #           n! because we will process n! permutations of edges
    #           *e because potentially for each call we remove and return all edges
    in_degree = {}
    neighbors = {}

    for prerequisite in prerequisites:
        if prerequisite[0] not in in_degree:
            in_degree[prerequisite[0]] = 0

        if prerequisite[1] not in in_degree:
            in_degree[prerequisite[1]] = 0

        if prerequisite[0] not in neighbors:
            neighbors[prerequisite[0]] = []

        if prerequisite[1] not in neighbors:
            neighbors[prerequisite[1]] = []

        in_degree[prerequisite[1]] += 1
        neighbors[prerequisite[0]].append(prerequisite[1])

    queue = []

    for vertex, count in in_degree.items():
        if count == 0:
            queue.append(vertex)

    results = []

    _get_topological_orderings(in_degree, neighbors, queue, results, [])

    return results


def _get_topological_orderings(in_degree: dict[int, int],
                               neighbors: dict[int, list[int]],
                               queue: list[int],
                               results: list[list[int]],
                               result: list[int]) -> None:
    """Recursive helper function"""
    if queue:
        for vertex in queue:
            result.append(vertex)  # E.g. image our queue is [0, 1]

            queue_for_next_call = queue.copy()
            queue_for_next_call.remove(vertex)  # Now queue is just [1], result is [3, 2, 0]

            for neighbor in neighbors[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue_for_next_call.append(neighbor)

            _get_topological_orderings(in_degree, neighbors, queue_for_next_call,
                                       results, result)

            result.remove(vertex)  # Now backtrack, removing 0 from result [3, 2], next 1 will be appended

            for neighbor in neighbors[vertex]:
                in_degree[neighbor] += 1

    if len(result) == len(in_degree.keys()):
        results.append(result.copy())


def alien_dictionary(words: list[str]) -> str:
    """
    There is a dictionary containing words from an alien language for which we don’t
    know the ordering of the letters. Write a method to find the correct order of the
    letters in the alien language. It is given that the input is a valid dictionary
    and there exists an ordering among its letters.

    Example:
        [ba, bc, ac, cab] -> bac
        - From ba, bc, we know a>c
        - from bc, ac, we know b>a
        - from ac, cab, we know a>c
    """
    # Solution:
    # - we can compare pairs of words until we find the first differing letter
    # - When the first letter differs, we add an edge between those 2 letters
    # - Then we can work out in-degree and neighbors, and topo sort like normal
    if len(words) <= 1:
        return ''

    # Stores the list of edges between characters
    edges = []

    for i in range(1, len(words)):
        word1 = words[i-1]
        word2 = words[i]

        min_len = min(len(word1), len(word2))

        for j in range(min_len):
            if word1[j] != word2[j]:
                edges.append([word1[j], word2[j]])
                break  # Found a non-matching char

    in_degree = {}
    neighbors = {}

    for edge in edges:
        if edge[0] not in in_degree:
            in_degree[edge[0]] = 0

        if edge[1] not in in_degree:
            in_degree[edge[1]] = 0

        if edge[0] not in neighbors:
            neighbors[edge[0]] = []

        if edge[1] not in neighbors:
            neighbors[edge[1]] = []

        in_degree[edge[1]] += 1
        neighbors[edge[0]].append(edge[1])

    queue = deque()

    for vertex, count in in_degree.items():
        if count == 0:
            queue.append(vertex)

    result = ''

    while queue:
        vertex = queue.popleft()
        result += vertex

        for neighbor in neighbors[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result


def reconstruct_sequence(original_sequence: list[int], sequences: list[list[int]]) -> bool:
    """
    Given a sequence originalSeq and an array of sequences, write a method to find if
    originalSeq can be uniquely reconstructed from the array of sequences.

    Unique reconstruction means that we need to find if originalSeq is the only sequence such that all
    sequences in the array are subsequences of it.

    [1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]] -> True
    """
    edges = []

    for sequence in sequences:
        for i in range(1, len(sequence)):
            edges.append([sequence[i-1], sequence[i]])

    in_degree = {}
    neighbors = {}

    for edge in edges:
        if edge[0] not in in_degree:
            in_degree[edge[0]] = 0

        if edge[1] not in in_degree:
            in_degree[edge[1]] = 0

        if edge[0] not in neighbors:
            neighbors[edge[0]] = []

        if edge[1] not in neighbors:
            neighbors[edge[1]] = []

        in_degree[edge[1]] += 1
        neighbors[edge[0]].append(edge[1])

    queue = deque()

    for vertex, count in in_degree.items():
        if count == 0:
            queue.append(vertex)

    result = []

    while queue:
        if len(queue) > 1:
            return False  # We have multiple orderings

        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in neighbors[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return len(result) == len(in_degree.keys())
