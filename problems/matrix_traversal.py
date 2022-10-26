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


def count_closed_islands(matrix: List[List[int]]) -> int:
    """
    A closed island is an island that is totally surrounded by 0s (i.e., water).
    This means all horizontally and vertically connected cells of a closed island are water.
    This also means that, by definition, a closed island can't touch an edge
    (as then the edge cells are not connected to any water cell).

    Write a function to find the number of closed islands in the given matrix.
    """
    closed_islands = 0

    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[False for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1 and not visited[row][col]:
                if _count_closed_islands_dfs(matrix, visited, row, col):
                    closed_islands += 1

    return closed_islands


def _count_closed_islands_dfs(matrix: List[List[int]], visited: List[List[bool]], row: int, col: int) -> bool:
    """Recursive helper function."""
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return False

    if visited[row][col]:
        return True

    if matrix[row][col] == 0:
        return True

    visited[row][col] = True

    return (_count_closed_islands_dfs(matrix, visited, row+1, col) and
            _count_closed_islands_dfs(matrix, visited, row-1, col) and
            _count_closed_islands_dfs(matrix, visited, row, col+1) and
            _count_closed_islands_dfs(matrix, visited, row, col-1))


def island_perimeter(matrix: List[List[int]]) -> int:
    """
    You are given a 2D matrix containing only 1s (land) and 0s (water).

    An island is a connected set of 1s (land) and is surrounded by either
    an edge or 0s (water). Each cell is considered connected to other cells
    horizontally or vertically (not diagonally).

    The given matrix has only one island, write a function to find the perimeter
    of that island.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for col in range(cols)] for row in range(rows)]

    perimeter_size = 0

    for row in range(rows):
        for col in range(cols):
            if not visited[row][col] and matrix[row][col]:
                perimeter_size = _island_perimeter_dfs(matrix, visited, row, col)
                break

    return perimeter_size


def _island_perimeter_dfs(matrix: List[List[int]], visited: List[List[bool]], row: int, col: int) -> int:
    """Recursive helper function."""
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return 1

    if matrix[row][col] == 0:
        return 1

    if visited[row][col]:
        return 0

    visited[row][col] = True

    perimeter = 0

    perimeter += _island_perimeter_dfs(matrix, visited, row+1, col)
    perimeter += _island_perimeter_dfs(matrix, visited, row-1, col)
    perimeter += _island_perimeter_dfs(matrix, visited, row, col+1)
    perimeter += _island_perimeter_dfs(matrix, visited, row, col-1)

    return perimeter


def count_distinct_islands(matrix: List[List[int]]) -> int:
    """
    Count the number of islands with a distinct shape.

    Solution:
    - Store a traversal string in a set.
    - Return the length of the set.

    Time: O(m*n)
    Space: O(m*n)
    """
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for col in range(cols)] for row in range(rows)]
    island_patterns = set()

    for row in range(rows):
        for col in range(cols):
            if not visited[row][col] and matrix[row][col] == 1:
                pattern = _distinct_islands_dfs(matrix, visited, row, col, 'S')  # Start
                island_patterns.add(pattern)

    return len(island_patterns)


def _distinct_islands_dfs(matrix: List[List[int]], visited: List[List[bool]], row: int, col: int, direction: str) -> str:
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return ''

    if visited[row][col] or matrix[row][col] == 0:
        return ''

    visited[row][col] = True

    # If we returned earlier, previous direction would be forgotten.
    # E.g. [1, 0] -> pattern += _dfs(...'R') -> pattern += ''
    pattern = direction
    pattern += _distinct_islands_dfs(matrix, visited, row+1, col, 'U')
    pattern += _distinct_islands_dfs(matrix, visited, row-1, col, 'D')
    pattern += _distinct_islands_dfs(matrix, visited, row, col+1, 'R')
    pattern += _distinct_islands_dfs(matrix, visited, row, col-1, 'L')

    # pattern += 'B'  # Go back

    return pattern
