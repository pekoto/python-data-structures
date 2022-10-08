from typing import List


def knapsack(max_weight: int, values: List[int], weights: List[int]) -> int:
    """A DP implementation of the knapsack problem.

    Given a knapsack that can hold max_weight, and a list of item values and weights,
    what is the max value that can be held in the knapsack?
    Example:
    max_weight = 10
    values  = [10, 40, 30, 50]
    weights = [ 5,  4,  6,  3]
    max_value = 90 (40+50 = weights 3+4)

    We solve this by constructing a matrix where item index is the row index,
    and capacity is the columns.

    Now, for each item, we decide whether to take it or not using the following formula:
    Max of:
    - Take it  = item weight + max weight of remaining capacity (given by row above)
    - Leave it = weight in row above

                [CAPACITY]
        0  1  2  3   4   5   6   7   8   9  10
    0 [[0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0],
    1 [0, 0, 0,  0,  0, 10, 10, 10, 10, 10, 10],
    2 [0, 0, 0,  0, 40, 40, 40, 40, 40, 50, 50],  [ITEM]
    3 [0, 0, 0,  0, 40, 40, 40, 40, 40, 50, 70],
    4 [0, 0, 0, 50, 50, 50, 50, 90, 90, 90, 90]]

    Time: O(max_weight*items)
    Space: O(max_weight*items)
    """
    rows = len(values) + 1  # +1 for 0 row (rows = item index)
    cols = max_weight + 1   # +1 for 0 col (columns = possible weight)
    matrix = [[0]*cols for i in range(rows)]

    # At row 0, we have no items, so value must be 0.
    # Similarly, at col 0, we have 0 weight, so value must be 0.
    for item in range(1, rows):
        for capacity in range(1, cols):

            # Value without this item is given by value in the row above.
            max_val_without_current_item = matrix[item-1][capacity]
            max_val_with_current_item = 0
            weight_of_current_item = weights[item-1]

            # Can we carry the current item?
            if capacity >= weight_of_current_item:
                max_val_with_current_item = values[item-1]
                remaining_capacity = capacity - weight_of_current_item
                # Check row above to see how much we can carry with remaining capacity.
                max_val_with_current_item += matrix[item-1][remaining_capacity]

            matrix[item][capacity] = max(max_val_with_current_item, max_val_without_current_item)

    # Finally, return the value in the lower right of the DP matrix
    return matrix[-1][-1]