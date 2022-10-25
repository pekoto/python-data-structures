from typing import List


def count_islands(matrix: List[List[int]]) -> int:
    """
    Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water),
    count the number of islands in it.

    Time: O(m*n)
    Space: O(m*n) [Can be O(1) if we can modify the matrix]
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    visited = [[False for col in range(num_cols)] for row in range(num_rows)]
    num_islands = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if not visited[row][col] and matrix[row][col] == 1:
                num_islands += 1
                _count_islands_dfs(matrix, visited, row, col)

    return num_islands


def _count_islands_dfs(matrix: List[List[int]], visited: List[List[bool]], row: int, col: int) -> None:
    """Recursive helper method."""

    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return

    if visited[row][col] or matrix[row][col] != 1:
        return

    visited[row][col] = True

    _count_islands_dfs(matrix, visited, row+1, col)
    _count_islands_dfs(matrix, visited, row-1, col)
    _count_islands_dfs(matrix, visited, row, col+1)
    _count_islands_dfs(matrix, visited, row, col-1)


def biggest_island(matrix: List[List[int]]) -> int:
    """
    Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water),
    find the biggest island in it. Write a function to return the area of the biggest island.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for col in range(cols)] for row in range(rows)]
    biggest_island = 0

    for row in range(rows):
        for col in range(cols):
            if not visited[row][col] and matrix[row][col] == 1:
                island_size = _biggest_island_dfs(matrix, visited, row, col)
                biggest_island = max(biggest_island, island_size)

    return biggest_island


def _biggest_island_dfs(matrix: List[List[int]], visited: List[List[bool]], row: int, col: int) -> int:
    """Recursive helper functions."""
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return 0

    if visited[row][col] or matrix[row][col] == 0:
        return 0

    visited[row][col] = True

    size = 1
    size += _biggest_island_dfs(matrix, visited, row+1, col)
    size += _biggest_island_dfs(matrix, visited, row-1, col)
    size += _biggest_island_dfs(matrix, visited, row, col+1)
    size += _biggest_island_dfs(matrix, visited, row, col-1)

    return size


def flood_fill(matrix: List[List[int]], x: int, y: int, new_col: int) -> None:
    """
    Any image can be represented by a 2D integer array (i.e., a matrix)
    where each cell represents the pixel value of the image.

    Flood fill algorithm takes a starting cell (i.e., a pixel) and a color.
    The given color is applied to all horizontally and vertically connected
    cells with the same color as that of the starting cell. Recursively, the
    algorithm fills cells with the new color until it encounters a cell with a
    different color than the starting cell.
    """
    target_col = matrix[x][y]

    _flood_fill(matrix, target_col, new_col, x, y)


def _flood_fill(matrix: List[List[int]], target_col: int, new_col: int, row: int, col: int) -> None:
    """Recursive helper function."""
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return

    if matrix[row][col] != target_col:
        return

    matrix[row][col] = new_col

    _flood_fill(matrix, target_col, new_col, row+1, col)
    _flood_fill(matrix, target_col, new_col, row-1, col)
    _flood_fill(matrix, target_col, new_col, row, col+1)
    _flood_fill(matrix, target_col, new_col, row, col-1)
