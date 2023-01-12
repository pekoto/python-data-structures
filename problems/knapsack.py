
def knapsack(values: list[int], weights: list[int], max_weight: int) -> int:
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
    rows = len(values)+1  # +1 for 0 value
    cols = max_weight+1  # +1 for 0 weight
    matrix = [[0]*cols for i in range(rows)]

    # At row 0, we have no item, so value must be 0
    # Similarly, for 0 capacity, we can't take any item
    for item in range(1, rows):
        for capacity in range(1, cols):

            max_value_without_item = matrix[item-1][capacity]  # Without this item, check row above
            max_value_with_current_item = 0
            weight_of_current_item = weights[item-1]

            # Can we carry the current item?
            if capacity >= max_weight:
                max_value_with_current_item = values[item-1]
                remaining_capacity = capacity-weight_of_current_item
                max_value_with_current_item += matrix[item-1][remaining_capacity]

            matrix[item][capacity] = max(max_value_without_item, max_value_with_current_item)

    return matrix[-1][-1]


def equal_subset_partition(nums: list[int]) -> bool:
    """
    Given a set of positive numbers, find if we can partition it into two
    subsets such that the sum of elements in both subsets is equal.

    Examples:
    [1, 2, 3, 4] -> True ([1, 4], [2, 3])
    [1, 1, 3, 4, 7] -> True ([1, 3, 4], [1, 7]
    [2, 3, 4, 6] -> False

    Solution:
    1. We are looking for a subset of size sum(nums)/2
    2. To find this, we recurse taking the number, and not taking the number
    3. To save overlapping subproblems, we can cache the result of each subarray and sum

    Time: O(n * sum(nums))
    Space: O(n * sum(nums))
    """
    total = sum(nums)

    if total % 2 != 0:
        # Cannot split into 2 if sum is odd.
        return False

    dp_cache = [[False for x in range((total//2) + 1)] for y in range(len(nums))]

    return _can_partition_subsets(dp_cache, nums, total//2, 0)


def _can_partition_subsets(dp_cache: list[list[int]], nums: list[int], target: int, index: int) -> bool:
    """Recursive helper function."""
    # nums: 1, 2, 3, 4, target: 5, index: 0
    # > target: 4, index: 1
    # >> target: 2, index: 2
    # >>> False
    # > target: 5, index: 1
    # >> target: 3, index: 2
    # >>> target: 0, index: 3, return True
    # Then cache: from [5][1] and [3][2] and [0][3], we can make target
    #       0  1  2  3  4  5
    #     0 F  F  F  F  F  F
    #     1 F  F  F  F  F  F
    #     2 F  F  F  F  F  F
    #     3 F  F  F  F  F  F
    if target == 0:
        return True

    if len(nums) == 0 or index >= len(nums):
        return False

    # We have not solved subproblem already
    if not dp_cache[index][target]:
        if nums[index] <= target:
            # Recursive call, decreasing sum and incrementing index
            if _can_partition_subsets(dp_cache, nums, target-nums[index], index+1):
                dp_cache[index][target] = True
                return True

    # Recursive call, excluding number at current index
    dp_cache[index][target] = _can_partition_subsets(dp_cache, nums, target, index+1)

    return dp_cache[index][target]


def subset_sum(nums: list[int], target: int) -> bool:
    """
    Given a set of positive numbers, determine if a subset exists whose sum is equal
    to a given number ‘S’.

    [1, 2, 3, 7], 6 -> True (1, 2, 3)
    [1, 2, 7, 1, 5], 10 -> True (1, 2, 7)
    [1, 3, 4, 8], 6 -> False
    """
    # Basic solution should be as before: We recurse with and without the number.
    # And we cache the results.
    rows = len(nums)+1
    cols = target+1
    dp = [[False]*cols for row in range(rows)]

    return _has_subset_sum(nums, target, 0, dp)


def _has_subset_sum(nums: list[int], target: int, index: int, dp: list[list[bool]]) -> bool:
    """Recursive helper function."""
    if target == 0:
        return True

    if len(nums) == 0 or index >= len(nums):
        return False

    if not dp[index][target]:
        if nums[index] <= target:
            if _has_subset_sum(nums, target - nums[index], index + 1, dp):
                dp[index][target] = True
                return True

    dp[index][target] = _has_subset_sum(nums, target, index+1, dp)

    return dp[index][target]


def minimum_subsets(nums: list[int]) -> int:
    """
    Given a set of positive numbers, partition the set into two subsets with minimum
    difference between their subset sums.

    [1, 2, 3, 9] -> 3 ([1, 2, 3], [9])
    [1, 2, 7, 1, 5] -> 0 ([1, 2, 5], [7, 1]
    [1, 3, 100, 4] -> 92 ([1, 3, 4], [100]
    """
    #     diff1              diff2
    # 1:          [1, 0]             |           [0, 1]
    # 2:     [2, 0]        [1, 2]    |    [2, 3]        [0, 3]
    # 3: [5, 0] [2, 3] [4, 2] [1, 5] | [3, 5] [2, 6] [3, 3] [0, 6]
    # 9: [14, 0] [5, 9] [11, 3] [2, 12] [10, 5] [1, 14] | [12, 5] [3, 14] [11, 6] [2, 15] [12, 3] [3, 12] [9, 6] [0, 15]
    # df:  14       4      8      10       5      13         7       11      5       13      9      9       3       15
    return _get_min_difference(nums, 0, 0, 0)


def _get_min_difference(nums: list[int], sum1: int, sum2: int, index: int) -> int:
    """Recursive helper function."""
    if index >= len(nums):
        return abs(sum1-sum2)

    diff1 = _get_min_difference(nums, sum1+nums[index], sum2, index+1)
    diff2 = _get_min_difference(nums, sum1, sum2+nums[index], index+1)

    return min(diff1, diff2)


def count_subset_sum(nums: list[int], target: int) -> int:
    """
    Given a set of positive numbers, find the total number of subsets whose sum is
    equal to a given number ‘S’.

    [1, 1, 2, 3], 4 -> 3 (1, 1, 2), (3, 1), (3, 1)
    """
    # We try recursing adding the number, and not adding the number.
    # This essentially gives us every subset permutation.
    # 1: [1]                             | [0]
    # 1: [2] [1]                         | [1] [0]
    # 2: [4] [2] [3] [1]                 | [3] [1] [2] [0]
    # 3: [7] [4] [5] [2] [6] [3] [4] [1] | [6] [3] [4] [1] [5] [2] [3] [0]
    # Time: O(2^n) -- double each time
    # Space: O(n) -- recursion stack
    # Can be optimized by top-down memoization: store [index][sum] array.
    # Can also be optimized by bottom-up dynamic programming.
    return _count_subset_sums(nums, 0, target, 0)


def _count_subset_sums(nums: list[int], sum_so_far: int, target: int, index: int) -> int:
    """Recursive helper function."""
    if index >= len(nums):
        if sum_so_far == target:
            return 1
        else:
            return 0

    count = 0
    count += _count_subset_sums(nums, sum_so_far+nums[index], target, index+1)
    count += _count_subset_sums(nums, sum_so_far, target, index+1)

    return count
