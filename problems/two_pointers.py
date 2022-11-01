from typing import List
from collections import deque


def target_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of sorted numbers and a target sum,
    find a pair in the array whose sum is equal to the given target.

    Write a function to return the indices of the two numbers (i.e. the pair)
    such that they add up to the given target.
    """
    start = 0
    end = len(nums)-1

    while end > start:
        sum = nums[start] + nums[end]
        if sum == target:
            return [start, end]
        elif sum < target:
            start += 1
        else:
            # sum > target
            end -= 1

    return [-1, -1]


def remove_duplicates(nums: List[int]) -> int:
    """
    Given an array of sorted numbers, remove all duplicate number instances from it in-place,
    such that each element appears only once. The relative order of the elements should be
    kept the same and you should not use any extra space so that that the solution have a
    space complexity of O(1).

    Move all the unique elements at the beginning of the array and after moving return the
    length of the subarray that has no duplicate in it.
    """
    if len(nums) <= 1:
        return len(nums)

    start = 0

    for end in range(len(nums)):

        if nums[end] != nums[start]:
            start += 1
            nums[start] = nums[end]

    return start + 1


def remove_key(nums: List[int], key: int) -> int:
    """
    ven an unsorted array of numbers and a target ‘key’,
    remove all instances of ‘key’ in-place and return the new length of the array.
    """
    # Input: [11, 1, 2, 2, 1], Key=2, Output: 4
    #                ^
    #                       ^
    start = 0

    for end in range(len(nums)):
        if nums[end] != key:
            nums[start] = nums[end]
            start += 1

    return start


def square_sorted_array(nums: List[int]) -> List[int]:
    """
    Given a sorted array, create a new array containing squares of all
    the numbers of the input array in the sorted order.
    """
    # [-2, -1, 0, 2, 3]
    #          ^
    #          ^
    left = 0
    right = len(nums)-1

    squares = deque()

    while left <= right:
        left_square = nums[left]**2
        right_square = nums[right]**2

        if right_square > left_square:
            squares.appendleft(right_square)
            right -= 1
        else:
            squares.appendleft(left_square)
            left += 1

    return list(squares)


def triplet_sum_to_zero(nums: List[int]) -> List[List[int]]:
    """
    Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

    Input: [-3, 0, 1, 2, -1, 1, -2]
    Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
    """
    # Dumb approach: Just a 3 layer loop, O^3. Can we do better?
    # First, sort
    # [-3, -2, -1, 0, 1, 1, 2]
    #   ^             ^
    #                       ^
    #  First sort: o(n log n)
    # Put the pointer through the array, then use 2 sum to reach target
    # n^2 -- for each n, I go through the rest of the array n times
    nums.sort()

    result = []

    for i in range(len(nums)-2):

        start = i+1
        end = len(nums)-1

        if i > 0 and nums[i] == nums[i-1]:
            continue

        while start < end:
            total = nums[i] + nums[start] + nums[end]

            if total == 0:
                result.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1
                # Skip dupes
                while start < end and nums[start] == nums[start-1]:
                    start += 1
                while start < end and nums[end] == nums[end+1]:
                    end -= 1
            elif total > 0:
                end -= 1
            else:
                # total < 0
                start += 1

    return result
