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
