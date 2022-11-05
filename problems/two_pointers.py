from typing import List
from collections import deque
import sys


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
    Given an unsorted array of numbers and a target ‘key’,
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


def triplet_sum_closest_to_target(nums: List[int], target: int) -> int:
    """
    Given an array of unsorted numbers and a target number, find a triplet in the
    array whose sum is as close to the target number as possible, return the sum
    of the triplet. If there are more than one such triplet, return the sum of the
    triplet with the smallest sum.

    Input: [-2, 0, 1, 2], target=2
    Output: 1
    Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
    """
    # [-2, 0, 1, 2]
    #   ^
    #         ^
    #             ^
    # 1. We can use the 3 pointer approach, keeping closest to target
    # But how to find the smallest sum? We need to store SUM and smallest difference
    smallest_sum = sys.maxsize
    smallest_diff = sys.maxsize

    for i in range(len(nums)-2):

        start = i+1
        end = len(nums)-1

        while start < end:
            current_sum = nums[i] + nums[start] + nums[end]
            diff = abs(target-current_sum)

            if diff < smallest_diff:
                smallest_sum = current_sum
                smallest_diff = diff

            if diff == smallest_diff and current_sum < smallest_sum:
                smallest_sum = current_sum

            if current_sum < target:
                start += 1
            elif current_sum > target:
                end -= 1
            else:
                # current_sum == target
                return 0

    return smallest_sum


def product_less_than_target(nums: List[int], target: int) -> List[int]:
    """
    Given an array with positive numbers and a positive target number,
    find all of its contiguous subarrays whose product is less than the target number.

    [2, 5, 3, 10], target=30
              ^
               ^
     product=2

    [2], [5], [2, 5], [3], [5, 3], [10]
    """
    result = []
    start = 0
    product = 1

    for end in range(len(nums)):
        product *= nums[end]

        while product >= target and start < len(nums):
            product /= nums[start]
            start += 1

        # Now we know that all subarrays from left>right have
        # product < target. To avoid dupes, we start with subarray
        # containing only right and then extend left.
        temp_list = deque()
        for i in range(end, start-1, -1):
            temp_list.appendleft(nums[i])
            result.append(list(temp_list))

    return result


def dutch_national_flag(nums: List[int]) -> None:
    """
    Given an array containing 0s, 1s and 2s, sort the array in-place.
    You should treat numbers of the array as objects, hence, we can’t
    count 0s, 1s, and 2s to recreate the array.

    Input: [1, 0, 2, 1, 0]
    Output: [0 0 1 1 2]
    """
    low_pointer = 0
    high_pointer = len(nums)-1

    i = 0

    while i <= high_pointer:

        if nums[i] == 1:
            i += 1
        elif nums[i] == 0:
            nums[i], nums[low_pointer] = nums[low_pointer], nums[i]
            i += 1
            low_pointer += 1
        elif nums[i] == 2:
            nums[i], nums[high_pointer] = nums[high_pointer], nums[i]
            high_pointer -= 1


def compare_backspaces(str1: str, str2: str) -> bool:
    """
    Given two strings containing backspaces (identified by the character ‘#’),
    check if the two strings are equal.

    Example 1:

    Input: str1="xy#z", str2="xzz#" = Output: true
    After applying backspaces the strings become "xz" and "xz" respectively.
    """

    # xy#z
    #    ^
    # xyz#
    #  ^
    i = len(str1)-1
    j = len(str2)-1

    while i >= 0 and j >= 0:
        str1_backspace_count = 0
        while i >= 0 and str1[i] == '#':
            str1_backspace_count += 1
            i -= 1

        i -= str1_backspace_count

        str2_backspace_count = 0
        while j >= 0 and str2[j] == '#':
            str2_backspace_count += 1
            j -= 1

        j -= str2_backspace_count

        if i < 0 and j < 0:
            return True

        if i < 0 or j < 0:
            return False

        if str1[i] != str2[j]:
            return False

        i -= 1
        j -= 1

    return True


def minimum_window_sort(nums: List[int]) -> int:
    """
    Given an array, find the length of the smallest subarray in it
    which when sorted will sort the whole array.

    Input: [1, 2, 5, 3, 7, 10, 9, 12], Output: 5
    We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted.
    """
    # [1, 2, 5, 3, 7, 10, 9, 12]
    #        ^
    #                       ^
    # start point = bigger than number after it
    # if i < len(nums) -1 and nums[i] > nums[i+1]
    # end point = bigger number than before, going backwards
    # [10, 0, 1, 2]
    # Find the lower number out of order.
    # Where should it go? That's the start.
    # Find the highest number out of order.
    # Where should it go? That's the end.
    start = 0
    end = 0

    smallest_num = sys.maxsize
    largest_num = -sys.maxsize-1

    # First, find the smallest number out of order
    for i in range(len(nums)):
        if i > 0 and nums[i] < nums[i-1]:
            if nums[i] < smallest_num:
                end = i
                smallest_num = nums[i]

            if nums[i] > largest_num:
                end = i
                largest_num = nums[i]

    if smallest_num == sys.maxsize:
        # List is sorted
        return 0

    # Now end should be set,
    # but we need to find where the smallest num should go
    for i in range(len(nums)):
        if nums[i] > smallest_num:
            start = i
            break

    return (end-start)+1
