from typing import List


def cyclic_sort_a(nums: List[int]) -> None:
    """
    Sort a list of numbers in place, where the list of numbers are 1-n

    Example:
        [3, 1, 5, 4, 2]
        [1, 2, 3, 4, 5]

    Time: O(n)
        Outer loop runs O(n)
        Worst case, inner loop would do O(n) swaps, but a swap puts a number
        in the correct place, so this would only happen once, giving us O(n) + O(n).
    Space: O(1)
    """
    i = 0
    while i < len(nums):

        correct_index = nums[i] - 1  # E.g. 3 should be at index 2
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1


def find_missing(nums: List[int]) -> int:
    """
    We are given an array containing n distinct numbers taken from the range 0 to n.
    Since the array has only n numbers out of the total n+1 numbers, find the missing number.

    Input: [4, 0, 3, 1]
    Output: 2

    Time: O(n)
    Space: O(1)
    """
    # First, swap the numbers using cyclic sort.
    i = 0
    while i < len(nums):  # Point: Don't increment every cycle. Use while.
        if nums[i] >= len(nums):
            i += 1  # Number is out of range.
        elif nums[i] == i:
            i += 1  # Number is in the right place.
        else:
            correct_index_val = nums[i]
            nums[i], nums[correct_index_val] = nums[correct_index_val], nums[i]

    # Next, find number in wrong position.
    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return -1  # No number missing.


def find_missing_numbers(nums: List[int]) -> List[int]:
    """
    We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
    The array can have duplicates, which means some numbers will be missing.
    Find all those missing numbers.

    Input: [2, 3, 1, 8, 2, 3, 5, 1], Output: 4, 6, 7
    """
    # I think we just check: If the number in the target is already correct, skip on
    i = 0
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1  # In correct place.
        elif nums[i] == nums[nums[i]-1]:
            i += 1  # Dupe in target place.
        else:
            correct_index = nums[i]-1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    missing = []

    for i in range(len(nums)):
        if nums[i] != i+1:
            missing.append(i+1)

    return missing


def find_duplicate_number(nums: List[int]) -> int:
    """
    We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
    The array has only one duplicate but it can be repeated multiple times.
    Find that duplicate number without using any extra space.
    You are, however, allowed to modify the input array.

    Input: [1, 4, 4, 3, 2]
    Output: 4
    """
    # [1, 4, 4, 3, 2]
    # [1, 4, 3, 4, 2]
    # Do cyclic sort: If the number is already in place, return.
    i = 0

    while i < len(nums):
        if nums[i] == i+1:
            i += 1
        elif nums[nums[i]-1] == nums[i]:
            return nums[i]  # Found the dupe
        else:
            correct_index = nums[nums[i]-1]
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    return -1


def find_duplicate_numbers(nums: List[int]) -> List[int]:
    """
    We are given an unsorted array containing n numbers taken from the range 1 to n.
    The array has some numbers appearing twice, find all these duplicate numbers using
    constant space.

    Input: [3, 4, 4, 5, 5]
    Output: [4, 5]
    """
    # [3, 4, 4, 5, 5]
    # [5, 4, 3, 4, 5]
    # [5, 4, 7, 2, 3, 5, 3]
    # [3, 2, 3, 4, 5, 5, 7]
    i = 0
    duplicates = []

    while i < len(nums):
        if nums[i] == i + 1:
            i += 1  # Number is in correct place
        elif nums[nums[i]-1] == nums[i]:
            i += 1  # Duplicate already in place
        else:
            correct_index = nums[i]-1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicates.append(nums[i])

    return duplicates


def find_corrupt_pair(nums: List[int]) -> List[int]:
    """
    We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
    The array originally contained all the numbers from 1 to ‘n’, but due to a data error,
    one of the numbers got duplicated which also resulted in one number going missing.
    Find both these numbers.

    Input: [3, 1, 2, 5, 2] -> Output: [2, 4]
    Explanation: '2' is duplicated and '4' is missing.
    """
    corrupt = []
    i = 0
    while i < len(nums):
        if nums[i] == i+1:
            i += 1  # Already in place
        elif nums[i] == nums[nums[i]-1]:
            i += 1  # Have a dupe
        else:
            correct_index = nums[i]-1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    for i in range(len(nums)):
        if nums[i] != i+1:
            corrupt.append(nums[i])
            corrupt.append(i+1)

    return corrupt


def find_smallest_missing_number(nums: List[int]) -> int:
    """
    Given an unsorted array containing numbers and a number ‘k’,
    find the first ‘k’ missing positive numbers in the array.

    Input: [3, -1, 4, 5, 5], k=3
    Output: [1, 2, 6]
    """
    # [5, -1, 5, 3, 4]  # Add as missing. Then fill up array from last number.
    # [4, 3, 2]  # Gets tricky. Brute force is hold every positive num in a set.

    # First we do a cyclic sort, skipping -ve or nums >= len(arr)
    i = 0
    while i < len(nums):
        if nums[i] < 0 or nums[i] >= len(nums):
            i += 1  # -ve or out of range num
        elif nums[i] == i:
            i += 1  # Already in place
        else:
            correct_index = nums[i]
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    # Next, starting from 1, if it doesn't match the index, it's potentially missing
    for i in range(1, len(nums)):
        if nums[i] != i:
            return i

    return len(nums)


def find_smallest_missing_k_numbers(nums: List[int], k: int) -> List[int]:
    """
    Given an unsorted array containing numbers, find the smallest missing positive number in it.
    Note: Positive numbers start from '1'.

    Example 1:

    Input: [-3, 1, 5, 4, 2] -> Output: 3
    """
    # First we do a cyclic sort, skipping -ve or nums >= len(arr)
    i = 0
    while i < len(nums):
        if nums[i] < 0 or nums[i] > len(nums):
            i += 1  # -ve or out of range num
        elif nums[i] == i or nums[i] == nums[nums[i]-1]:
            i += 1  # Already in place or dupe
        else:
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    extra_numbers = set()
    missing = []

    # Next, starting from 1, if it doesn't match the index, we return that index
    # If we reach the end of the array, we return len(arr)
    for i in range(len(nums)):
        if nums[i] != i+1:
            missing.append(i+1)
            extra_numbers.add(nums[i])
            if len(missing) == k:
                break

    i = 1
    while len(missing) < k:
        target = len(nums)+i
        if target not in extra_numbers:
            missing.append(target)
        i += 1

    return missing
