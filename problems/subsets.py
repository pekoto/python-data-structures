from collections import deque
from typing import List


def generate_subsets(nums: List[int]) -> List[int]:
    """
    Given a set with distinct elements, find all of its distinct subsets.

    Example 1:
    Input: [1, 3] > Output: [], [1], [3], [1,3]

    Example 2:
    Input: [1, 5, 3] > Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

    Time: O(N*2^n) [For each number we double the number of subsets]
    Space: O(N*2^n)
    """
    # 1, 3
    # [] -> [], [1] -> [], [1], [3], [1, 3]
    # For every element, add the next element.

    subsets = []
    subsets.append([])  # Append the empty set

    for num in nums:

        for i in range(len(subsets)):
            subset = subsets[i].copy()
            subset.append(num)
            subsets.append(subset)

    return subsets


def subsets_with_duplicates(nums: List[int]) -> List[int]:
    """
    Given a set of numbers that might contain duplicates,
    find all of its distinct subsets.

    Example 1:
    Input: [1, 3, 3]
    Output: [], [1], [3], [1,3], [3,3], [1,3,3]

    Time: O(n*2^n)
    Space: O(n*2^n)
    """
    # When we have a duplicate, only add the subsets that were added in the last step.
    nums.sort()

    subsets = []
    subsets.append([])
    new_subsets_start_index = 0

    for i in range(len(nums)):

        # Assume we will process all subsets...
        start_index = 0

        if i > 0 and nums[i] == nums[i-1]:
            # ...Unless there is a dupe found.
            # Then just process from last subsets.
            start_index = new_subsets_start_index

        # Save the end index of the subsets we added last time
        # (Just before we start extending the list)
        # (Actually this is the place where we'll start adding new subsets)
        new_subsets_start_index = len(subsets)

        for j in range(start_index, len(subsets)):
            subset = subsets[j].copy()
            subset.append(nums[i])
            subsets.append(subset)

    return subsets


def generate_permutations(nums: List[int]) -> List[int]:
    """
    Given a set of distinct numbers, find all of its permutations.

    Input: [1,3,5]
    Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]

    Time: O(n*n!), n! permutations total. In each iteration, it takes n time to insert a number for each permutation.
    Space: O(n*n!)
    """
    # As subsets, but add in every position
    # []
    # [1]
    # [1, 3], [3, 1]
    # [5, 1, 3], [1, 5, 3], [1, 3, 5], [5, 3, 1], [3, 5, 1], [3, 1, 5]
    permutations = []
    queue = deque()
    queue.append([])

    for num in nums:

        for i in range(len(queue)):

            permutation = queue.popleft()

            for j in range(len(permutation)+1):
                new_permutation = permutation.copy()
                new_permutation.insert(j, num)

                if len(new_permutation) == len(nums):
                    permutations.append(new_permutation)
                else:
                    queue.append(new_permutation)

    return permutations


def case_permutations(s: str) -> List[str]:
    """
    Given a string, find all of its permutations preserving the character sequence but changing case.

    Input: "ad52"
    Output: "ad52", "Ad52", "aD52", "AD52"
    # ad52 > ad52 > ad52 > ad52
    #      > aD52 > aD52 > aD52
    # Ad52 > Ad52 > Ad52 > Ad52
    #        AD52 > AD52 > AD52
    """
    results = []
    _case_permutations(list(s), 0, results)

    return results


def _case_permutations(s: List[chr], index: int, result: List[str]) -> None:

    if index == len(s):
        result.append(''.join(s))
        return

    # Need to copy
    not_upper = s.copy()

    # Recurse changing this char to upper
    _case_permutations(not_upper, index+1, result)

    if not s[index].isdigit():
        with_upper = s.copy()
        with_upper[index] = with_upper[index].upper()

        # Recurse changing this not to upper
        # Str causing this to be weird and skip over...
        _case_permutations(with_upper, index+1, result)


def balanced_parentheses(n: int) -> List[str]:
    """
    For a given number ‘N’, write a function to generate all combination
    of ‘N’ pairs of balanced parentheses.

    Example:
    Input: N=3
    Output: ((())), (()()), (())(), ()(()), ()()()
    """
    results = []

    _balanced_parentheses(n, n, [], results)

    return results


def _balanced_parentheses(left_count: int, right_count: int, s: List[chr], results: List[str]) -> None:
    """Recursive helper function."""
    # left_count=2
    # right_count=2
    # [(, left_count=1
    #  [(, (] left_count = 0
    #    [(, (, ), )]
    #  [(, )] left_count=1, right_count=1
    #   [(, ), ()

    # If we don't have left or right brackets left, return.
    if left_count == 0 and right_count == 0:
        results.append(''.join(s))
        return

    # If we have equal numbers of left and right, we must add a left
    if left_count == right_count:
        s_copy = s.copy()
        s_copy.append('(')
        _balanced_parentheses(left_count-1, right_count, s_copy, results)
    elif left_count < right_count:
        # If left count < right count:
        # If left count is 0, we must add a right bracket
        # Otherwise, we can add a left bracket, AND a right bracket as 2 permutations
        if left_count == 0:
            s_copy = s.copy()
            s_copy.append(')')
            _balanced_parentheses(left_count, right_count-1, s_copy, results)
        else:
            s_copy_left = s.copy()
            s_copy_left.append('(')
            _balanced_parentheses(left_count-1, right_count, s_copy_left, results)

            s_copy_right = s.copy()
            s_copy_right.append(')')
            _balanced_parentheses(left_count, right_count-1, s_copy_right, results)


