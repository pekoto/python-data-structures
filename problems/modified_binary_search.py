from typing import List
import sys


def order_agnostic_binary_search(nums: List[int], key: int) -> int:
    """
    Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
    Though we know that the array is sorted, we don’t know if it’s sorted in ascending
    or descending order. You should assume that the array can have duplicates.

    Write a function to return the index of the ‘key’ if it is present in the array,
    Otherwise return -1.

    Input: [4, 6, 10], key=10 -> Output: 2

    Input: [10, 6, 4], key=10 -> Output: 0
    """
    reversed=False
    if nums[0] > nums[-1]:
        reversed = True

    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if key == nums[mid]:
            return mid
        elif key > nums[mid]:
            if reversed:
                right = mid-1
            else:
                left = mid+1
        else:
            # key < mid
            if reversed:
                left = mid+1
            else:
                right = mid-1

    return -1


def ceiling_number(nums: List[int], key: int) -> int:
    """
    Given an array of numbers sorted in an ascending order, find the ceiling of a given
    number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array
    greater than or equal to the ‘key’.

    Input: [4, 6, 10], key=6 -> Output: 1
    Input: [1, 3, 8, 10, 15], key=12 -> Output: 4
    Input: [4, 6, 10], key=17 -> Output: -1

    Note: This can be solved more easily: Just return left.
    """
    left = 0
    right = len(nums)-1
    min_diff = sys.maxsize
    ceiling = -1

    while left <= right:
        mid = (left+right) // 2

        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            left = mid+1
        else:
            # mid is > key
            if (nums[mid]-key) < min_diff:
                # Found a ceiling
                min_diff = nums[mid]-key
                ceiling=mid
            right = mid-1

    return ceiling


def next_letter(letters: List[chr], key: chr) -> chr:
    """
    Given an array of lowercase letters sorted in ascending order, find the
    smallest letter in the given array greater than a given ‘key’.

    Assume the given array is a circular list, which means that the last letter is
    assumed to be connected with the first letter. This also means that the smallest letter
    in the given array is greater than the last letter of the array and is also the first
    letter of the array.

    Write a function to return the next letter of the given ‘key’.

    Input: ['a', 'c', 'f', 'h'], key='f' -> Output: 'h'
    Input: ['a', 'c', 'f', 'h'], key='b' -> Output: 'c'
    Input: ['a', 'c', 'f', 'h'], key='m' -> Output: 'a'
    Input: ['a', 'c', 'f', 'h'], key='h' -> Output: 'a'
    """
    # If we find it and not at end of the array, return the next element
    # If we find it and we're at the end of the array, return the first element
    #   ['a', 'c', 'f', 'h'], key='b'
    # l:       ^
    # r:  ^
    # m:  ^
    # Return start works
    #    ['a', 'c', 'f', 'h'], key='m'
    # l:                      ^
    # r:                   ^
    # m:                   ^
    #    ['c', 'f', 'h'], key='a'
    # l:   ^
    # r: ^
    # m:   ^
    # If start > end of array, return 0
    left = 0
    right = len(letters)-1

    while left <= right:
        mid = (left + right) // 2

        if key == letters[mid]:
            # Found it
            if mid == len(letters)-1:
                # end of the array
                return letters[0]
            else:
                return letters[mid+1]
        elif key < letters[mid]:
            right = mid-1
        else:
            left = mid+1

    if left > len(letters)-1:
        return letters[0]
    else:
        return letters[left]


def number_range(nums: List[int], key: int) -> List[int]:
    """
    Given an array of numbers sorted in ascending order, find the range of a given number
    ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the
    array.

    Write a function to return the range of the ‘key’. If the ‘key’ is not present return
    [-1, -1].

    [4, 6, 6, 6, 9], key=6 -> [1, 3]
    [1, 3, 8, 10, 15], key=10 -> [3, 3]
    [1, 3, 8, 10, 15], key=12 -> [-1, -1]
    """
    # Brute force is O(n), so we have to do better than that.
    # What we do is binary search with a left bias:
    # When we find the number, we save it and then search left.
    # Then do the same for the right.
    left_index = _binary_search(nums, key, True)
    right_index = _binary_search(nums, key, False)

    return [left_index, right_index]


def _binary_search(nums: List[int], key: int, search_left: bool) -> int:
    """Recursive helper function."""
    found_index = -1
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right) //2

        if key < nums[mid]:
            right = mid-1
        elif key > nums[mid]:
            left = mid+1
        else:
            # Found it
            found_index = mid
            if search_left:
                right = mid-1
            else:
                # Search right
                left = mid+1

    return found_index


def min_difference(nums: List[int], key: int) -> int:
    """
    Given an array of numbers sorted in ascending order, find the element in
    the array that has the minimum difference with the given ‘key’.

    Input: [4, 6, 10], key=7 -> 6
    Input: [4, 6, 10], key=4
    """
    min_diff = sys.maxsize
    min_diff_elem = -1

    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == key:
            return nums[mid]
        elif key > nums[mid]:
            diff = abs(nums[mid] - key)
            if diff < min_diff:
                min_diff = diff
                min_diff_elem = nums[mid]
            left = mid+1
        else:
            # key < nums[mid]
            diff = abs(nums[mid] - key)
            if diff < min_diff:
                min_diff = diff
                min_diff_elem = nums[mid]
            right = mid-1

    return min_diff_elem


def bitonic_array_maximum(nums: List[int]) -> int:
    """
    Find the maximum value in a given Bitonic array. An array is considered bitonic if it
    is monotonically increasing and then monotonically decreasing. Monotonically increasing
    or decreasing means that for any index i in the array arr[i] != arr[i+1].

    [1, 3, 8, 12, 4, 2] -> 12
    [3, 8, 3, 1] -> 8
    [1, 3, 8, 12] -> 12
    [10, 9, 8] -> 10
    """
    # Else...
    # If we are in an ascending part
    # ...if we are on an ascening part (number to the right is greater), shift left = mid
    # ...if we are on a descending part (number to the right is less, shift right = mid
    left = 0
    right = len(nums)-1

    if nums[left] > nums[left+1]:
        return nums[left]

    if nums[right] > nums[right-1]:
        return nums[right]

    while left <= right:
        mid = (left + right) // 2

        # We have the pivot
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            # If we are in the middle of the array and nums to either size are smaller -> we got it
            return nums[mid]

        # We don't have the pivot
        elif nums[mid] < nums[mid+1]:
            # We're on an ascending part, move right
            left = mid+1
        else:
            # We're on a descending part, move left
            right = mid

    return -1


def search_bitonic_array(nums: List[int], key: int) -> int:
    """
    Given a Bitonic array, find if a given ‘key’ is present in it.
    An array is considered bitonic if it is monotonically increasing and then
    monotonically decreasing. Monotonically increasing or decreasing means that for
    any index i in the array arr[i] != arr[i+1].

    Write a function to return the index of the ‘key’. If the 'key' appears more than once,
    return the smaller index. If the ‘key’ is not present, return -1.

    [1, 3, 8, 4, 3], key=4 --> 3
    [3, 8, 3, 1], key=8 --> 1
    [1, 3, 8, 12], key=12 --> 3
    [10, 9, 8], key=10 --> 0
    """
    # Approach: find the pivot, binary search left, binary search right

    # First, find the pivot point
    left = 0
    right = len(nums)-1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid+1]:
            # We shift left up to match the pivot point if on an ascending
            # part
            left = mid+1
        else:
            # We shift right down to mid if we are on a descending part
            right = mid

    pivot_point = left
    search_left_result = _binary_search_bitonic(nums, key, 0, pivot_point, True)
    if search_left_result != -1:
        return search_left_result

    return _binary_search_bitonic(nums, key, pivot_point+1, len(nums)-1, False)


def _binary_search_bitonic(nums: List[int], key: int, left_start: int, right_start: int, ascending: bool) -> int:
    """Helper function."""
    left = left_start
    right = right_start

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == key:
            return mid
        elif key > nums[mid]:
            if ascending:
                left = mid+1
            else:
                right = mid-1
        else:
            if ascending:
                right = mid-1
            else:
                left = mid+1

    return -1


def search_rotated_array(nums: List[int], key: int) -> int:
    """
    Given an array of numbers which is sorted in ascending order and also rotated by some
    arbitrary number, find if a given ‘key’ is present in it.

    Write a function to return the index of the ‘key’ in the rotated array.
    If the ‘key’ is not present, return -1. You can assume that the given array does not
    have any duplicates.

    [10, 15, 1, 3, 8], key=15 -> 1
    [4, 5, 7, 9, 10, -1, 2], key=10 -> 4
    """
    # Approach: We can simply binary search the relevant half IF we know where the rotation point is
    # Finding the rotation point:
    # If left < right, then the array is sorted
    # if left < mid, then rotation point is somewhere in right half, set left = mid+1
    # if mid < right, then rotation point is somewhere in left half, set right = mid-1
    # [10, 15, 1, 3, 8]
    #  ^
    #       ^
    #  ^
    # rotation point is end (makes sense -- it must be the max number)
    # [4, 5, 7, 9, 10, -1, 2]
    #               ^
    #               ^
    #               ^
    # (There is a simplified solution: Check if the key is within the sorted range --
    #  basically, integrate the if conditions from the first loop into the second.)
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right) //2

        if nums[left] < nums[right]:
            break
        elif nums[left] < nums[right]:
            left = mid+1
        else:
            # mid < right
            right = mid-1

    rotation_point = right

    left = 0
    right = 0
    if key <= nums[rotation_point]:
        left = 0
        right = rotation_point
    else:
        left = rotation_point
        right = len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == key:
            return mid
        elif key < nums[mid]:
            right = mid-1
        else:
            left = mid+1

    return -1


def rotation_count(nums: List[int]) -> int:
    """
    Given an array of numbers which is sorted in ascending order and is rotated ‘k’
    times around a pivot, find ‘k’.

    You can assume that the array does not have any duplicates.

    [10, 15, 1, 3, 8] -> 2
    [4, 5, 6, 9, 10, -1, 2] -> 5
    """
    # Approach: Similar to our first question above, except return end+1
    left = 0
    right = len(nums)-1

    while left < right:
        mid = (left+right) // 2

        if nums[left] < nums[right]:
            break
        elif nums[left] < nums[mid]:
            # Left half sorted, move right
            left = mid+1
        else:
            # Right half sorted, move left
            right = mid-1

    if right == len(nums)-1:
        return 0

    return right+1
