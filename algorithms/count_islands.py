from typing import List


def count_islands(land: List[List[int]]) -> int:
    """Count the number of islands in a 2D matrix.

    Eg. 3 islands:
    land = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
        ]

    1. Iterate around rows and columns
    2. If we hit a 1 we haven't visited..
    3. DFS, incrementing the count

    Time: O(NxM)
    Space: O(NxM) [Could reduce space by updating matrix, but recursion stack would
        take the space.
    """
    count = 0
    num_rows = len(land)
    num_cols = len(land[0])

    visited = [[False for col in range(num_cols)] for row in range(num_rows)]

    for row in range(num_rows):
        for col in range(num_cols):
            if land[row][col] == 1 and not visited[row][col]:
                count += 1
                _dfs(land, visited, row, col)

    return count


def _dfs(land: List[List[int]], visited: List[List[bool]], row: int, col: int) -> None:
    """Recursive helper function."""

    if row < 0 or row >= len(land):
        return

    if col < 0 or col >= len(land[0]):
        return

    if visited[row][col] or land[row][col] != 1:
        return

    visited[row][col] = True

    _dfs(land, visited, row - 1, col)
    _dfs(land, visited, row + 1, col)
    _dfs(land, visited, row, col - 1)
    _dfs(land, visited, row, col + 1)
