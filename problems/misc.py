

def get_valid_partitions(s: str, words: set[str]) -> list[list[str]]:
    """
    Given a string and a list of valid words, return all of the valid partitions for the string.

    adage -> [["ad", "age"], ["adage"]]
    """
    if not s or not words:
        return []

    results = []

    _get_valid_partitions(s, words, 0, [], 0, results)

    return results


def _get_valid_partitions(s: str, words: set[str], start_pos: int, partition: list[str], partition_len: int, results: list[list[str]]) -> None:
    if start_pos >= len(s):
        if partition_len == len(s):
            results.append(partition.copy())
        return

    for i in range(start_pos, len(s)+1):
        substr = s[start_pos: i]
        if substr in words:
            partition.append(substr)
            partition_len += len(substr)
            _get_valid_partitions(s, words, i, partition, partition_len, results)
            partition_len -= len(substr)
            partition.pop()

    # Because we need to include the whole string, actually we don't have to try it without
    # _get_valid_partitions(s, words, start_pos+1, partition, partition_len, results)


def number_of_provinces(is_connected: list[list[int]]) -> int:
    """
    LeetCode 547

    There are n cities. Some of them are connected, while some are not. If city a is connected
    directly with city b, and city b is connected directly with city c, then city a is connected
    indirectly with city c.

    A province is a group of directly or indirectly connected cities and no other cities
    outside of the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city
    and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

    Return the total number of provinces.

    Ex. 1
    1--2   3
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2

    Ex. 2
    1  2  3
    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3

    Ex. 3
    1  2  3  4
    |       |
    ---------
    Input: isConnected = [[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]
    Output: 3
    """
    if not is_connected:
        return 0

    rows = len(is_connected)
    cols = len(is_connected[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    provinces = 0

    for row in range(rows):
        if not visited[row][0]:
            provinces += 1
            _dfs(is_connected, visited, row)

    return provinces


def _dfs(is_connected: list[list[int]], visited: list[list[bool]], row: int) -> None:

    for col in range(0, len(is_connected[0])):
        visited[row][col] = True
        if is_connected[row][col] == 1 and not visited[col][0]:
            _dfs(is_connected, visited, col)


def number_of_provinces_union_find(is_connected: list[list[int]]) -> int:
    """LeetCode 547."""
    if not is_connected:
        return 0

    provinces = len(is_connected)

    union_find = UnionFind(is_connected)

    for row in range(len(is_connected)):
        for col in range(len(is_connected[0])):
            if is_connected[row][col] == 1:
                if union_find.union(row, col):
                    provinces -= 1

    return provinces


class UnionFind:

    def __init__(self, is_connected: list[list[int]]):
        self._parents = [i for i in range(len(is_connected))]
        self._rank = [1] * len(is_connected)

    def find(self, index: int):
        parent = index

        while parent != self._parents[parent]:
            self._parents[parent] = self._parents[self._parents[parent]]  # path compression
            parent = self._parents[parent]

        return parent

    def union(self, index_1: int, index_2: int) -> bool:
        parent_1 = self.find(index_1)
        parent_2 = self.find(index_2)

        if parent_1 == parent_2:
            return False  # Already unioned

        if self._rank[parent_2] > self._rank[parent_1]:
            self._parents[parent_1] = parent_2
            self._rank[parent_2] += self._rank[parent_1]
        else:
            self._parents[parent_2] = parent_1
            self._rank[parent_1] += self._rank[parent_2]

        return True
