from typing import List


def binary_search(nums: List[int], key: int) -> int:
    """Finds the index of key in a list of sorted nums.

    1. Set up left & right
    2. While left <= right...
        - Get the mid
        - Update left or right depending on if key < or > arr[mid]
        - If mid found, return it

    Space: O(1)
    Time: O(log n)

    param nums: A sorted list of integers.
    param key: The key to find in the list of integers.
    """
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = left + (right-left)//2

        if key > nums[mid]:
            left = mid + 1
        elif key < nums[mid]:
            right = mid - 1
        else:
            return mid

    raise KeyError(f'Not found: {key}')
