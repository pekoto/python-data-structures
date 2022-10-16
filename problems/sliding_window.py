from typing import List


def max_sum_subarray(nums: List[int], k: int) -> int:
    """
    Given an array of positive numbers and a positive number ‘k,’
    find the maximum sum of any contiguous subarray of size ‘k’.

    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].
    """
    start = 0
    max_sum = 0
    window_sum = 0

    for end in range(len(nums)):
        window_sum += nums[end]

        if (end-start)+1 == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[start]
            start += 1

    return max_sum


def smallest_sum_subarray(nums: List[int], k: int) -> int:
    """
    Given an array of positive numbers and a positive number ‘S,’
    find the length of the smallest contiguous subarray whose sum is
    greater than or equal to ‘S’. Return 0 if no such subarray exists.

    Example 1:

    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
    """
    start = 0
    sum_so_far = 0
    smallest_window = len(nums)+1

    for end in range(len(nums)):
        sum_so_far += nums[end]

        while sum_so_far >= k:
            smallest_window = min(smallest_window, (end-start)+1)
            sum_so_far -= nums[start]
            start += 1

    if smallest_window == len(nums)+1:
        return 0

    return smallest_window
