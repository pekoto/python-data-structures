import math


def longest_common_substring(s1: str, s2: str) -> int:
    """
    Given two strings ‘s1’ and ‘s2’, find the length of the longest substring
    which is common in both the strings.

    Example:
        s1=abdca, s2=cbda -> 2 (bd)
        s1=passport, s2=ppsspt -> 3 (ssp)
    """
    # If the letters match, we return 1 + rest of string
    # Otherwise we try skipping 1 letter from each string.
    # Time: O(2^n)
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return _longest_common_substring(s1, s2, 0, 0, dp)


def _longest_common_substring(s1: str, s2: str, s1_index: int, s2_index: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if s1_index >= len(s1) or s2_index >= len(s2):
        return 0

    if dp[s1_index][s2_index] == -1:

        skip_both = 0
        if s1[s1_index] == s2[s2_index]:
            skip_both = 1 + _longest_common_substring(s1, s2, s1_index+1, s2_index+2, dp)

        skip_s1 = _longest_common_substring(s1, s2, s1_index+1, s2_index, dp)
        skip_s2 = _longest_common_substring(s1, s2, s1_index, s2_index+1, dp)

        dp[s1_index][s2_index] = max(skip_both, skip_s1, skip_s2)

    return dp[s1_index][s2_index]


def longest_common_substring_bottomup(s1: str, s2: str) -> int:
    """
    Given two strings ‘s1’ and ‘s2’, find the length of the longest substring
    which is common in both the strings.

    Example:
        s1=abdca, s2=cbda -> 2 (bd)
        s1=passport, s2=ppsspt -> 3 (ssp)
    """
    """
    Thinking about bottomup...
    if chars match = 1 + longest match
    - Longest match is given by upper left.
    
      c  b  d  a 
    a 0  0  0  1
    b 0  1  0  0
    d 0  0  2  0
    c 1  0  0  0
    a 0  0  0  1  
    """
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    max_len = 0

    for s1_index in range(1, len(s1)+1):
        for s2_index in range(1, len(s2)+1):
            if s1[s1_index-1] == s2[s2_index-1]:
                substr_len = 1 + dp[s1_index-1][s2_index-1]
                dp[s1_index][s2_index] = substr_len
                max_len = max(max_len, substr_len)

    return max_len


def longest_common_subsequence(s1: str, s2: str) -> int:
    """
    Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence
    which is common in both the strings.

    A subsequence is a sequence that can be derived from another sequence by deleting
    some or no elements without changing the order of the remaining elements.

    Example:
        s1=abdca, s2=cbda -> 3 (bda)
        s1=passport, s2=ppsspt -> 5 (psspt)
    """
    # Brute force:
    # if chars match, try 1 + rest of string
    # Else try skipping string 1, and skipping string 2
    # Take max of each
    return _longest_common_subsequence(s1, s2, 0, 0)


def _longest_common_subsequence(s1: str, s2: str, s1_index: int, s2_index: int) -> int:
    """Recursive helper function."""
    if s1_index >= len(s1) or s2_index >= len(s2):
        return 0

    if s1[s1_index] == s2[s2_index]:
        return 1 + _longest_common_subsequence(s1, s2, s1_index+1, s2_index+1)

    skip_1 = _longest_common_subsequence(s1, s2, s1_index+1, s2_index)
    skip_2 = _longest_common_subsequence(s1, s2, s1_index, s2_index+1)

    return max(skip_1, skip_2)


def longest_common_subsequence_topdown(s1: str, s2: str) -> int:
    """
    Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence
    which is common in both the strings.

    A subsequence is a sequence that can be derived from another sequence by deleting
    some or no elements without changing the order of the remaining elements.

    Example:
        s1=abdca, s2=cbda -> 3 (bda)
        s1=passport, s2=ppsspt -> 5 (psspt)
    """
    # Brute force:
    # if chars match, try 1 + rest of string
    # Else try skipping string 1, and skipping string 2
    # Take max of each
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return _longest_common_subsequence_topdown(s1, s2, 0, 0, dp)


def _longest_common_subsequence_topdown(s1: str, s2: str, s1_index: int, s2_index: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if s1_index >= len(s1) or s2_index >= len(s2):
        return 0

    if dp[s1_index][s2_index] == -1:

        if s1[s1_index] == s2[s2_index]:
            dp[s1_index][s2_index] = 1 + _longest_common_subsequence_topdown(s1, s2, s1_index+1, s2_index+1, dp)
        else:
            skip_1 = _longest_common_subsequence_topdown(s1, s2, s1_index+1, s2_index, dp)
            skip_2 = _longest_common_subsequence_topdown(s1, s2, s1_index, s2_index+1, dp)

            dp[s1_index][s2_index] = max(skip_1, skip_2)

    return dp[s1_index][s2_index]


def longest_common_subsequence_bottomup(s1: str, s2: str) -> int:
    """
    Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence
    which is common in both the strings.

    A subsequence is a sequence that can be derived from another sequence by deleting
    some or no elements without changing the order of the remaining elements.

    Example:
        s1=abdca, s2=cbda -> 3 (bda)
        s1=passport, s2=ppsspt -> 5 (psspt)
    """
    # Brute force:
    # if chars match, try 1 + rest of string
    # Else try skipping string 1, and skipping string 2
    # Take max of each
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    max_len = 0

    for s1_index in range(1, len(s1)+1):
        for s2_index in range(1, len(s2)+1):
            if s1[s1_index-1] == s2[s2_index-1]:
                # Chars match, so take longest so far
                # (longest for prev subseq)
                dp[s1_index][s2_index] = 1 + dp[s1_index-1][s2_index-1]
            else:
                # Chars don't match, so take longest holding s1 or s2 the same
                dp[s1_index][s2_index] = max(dp[s1_index-1][s2_index], dp[s1_index][s2_index-1])

            max_len = max(max_len, dp[s1_index][s2_index])

    return max_len


def min_deletions_insertions(s1: str, s2: str) -> tuple[int, int]:
    """
    Given strings s1 and s2, we need to transform s1 into s2 by deleting and
    inserting characters. Write a function to calculate the count of the minimum
    number of deletion and insertion operations.

    Example:
        s1=abdca, s2=cbda -> 2,1 (delete a and c -- 2, and insert c -- 1)
    """
    # Solution: This is the same problem as longest common subsequence
    # The difference is we do longest string - common subseq and shorted string - common subseq
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    longest_subseq = _min_deletions_insertions(s1, s2, 0, 0, dp)

    longest = s1 if len(s1) > len(s2) else s2
    shortest = s1 if len(s1) < len(s2) else s2
    # Deletions and insertions
    return len(longest)-longest_subseq, len(shortest)-longest_subseq


def _min_deletions_insertions(s1: str, s2: str, s1_index: int, s2_index: int, dp: list[list[int]]) -> int:
    """Recursive helper function. (longest common subsequence)"""
    if s1_index >= len(s1) or s2_index >= len(s2):
        return 0

    if dp[s1_index][s2_index] == -1:
        if s1[s1_index] == s2[s2_index]:
            dp[s1_index][s2_index] = 1 + _min_deletions_insertions(s1, s2, s1_index+1, s2_index+1, dp)
        else:
            skip_s1 = _min_deletions_insertions(s1, s2, s1_index+1, s2_index, dp)
            skip_s2 = _min_deletions_insertions(s1, s2, s1_index, s2_index+1, dp)

            dp[s1_index][s2_index] = max(skip_s1, skip_s2)

    return dp[s1_index][s2_index]


def longest_increasing_subsequence(nums: list[int]) -> int:
    """
    Given a number sequence, find the length of its Longest Increasing Subsequence
    (LIS). In an increasing subsequence, all the elements are in increasing order
    (from lowest to highest).

    Example:
        [4, 2, 3, 6, 10, 1, 12] -> 5 (2, 3, 6, 10, 12)
        [-4, 10, 3, 7, 15] -> 4 (-4, 3, 7, 15)
    """
    return _longest_increasing_subsequence(nums, 0, -1)


def _longest_increasing_subsequence(nums: list[int], current_index: int, previous_index: int) -> int:
    if current_index >= len(nums):
        return 0  # We at least have 1 number in our sequence

    with_this_index = 0
    if previous_index == -1 or nums[current_index] > nums[previous_index]:
        with_this_index = 1 + _longest_increasing_subsequence(nums, current_index+1, current_index)

    skip_this_index = _longest_increasing_subsequence(nums, current_index+1, previous_index)

    return max(with_this_index, skip_this_index)


def longest_increasing_subsequence_topdown(nums: list[int]) -> int:
    """
    Given a number sequence, find the length of its Longest Increasing Subsequence
    (LIS). In an increasing subsequence, all the elements are in increasing order
    (from lowest to highest).

    Example:
        [4, 2, 3, 6, 10, 1, 12] -> 5 (2, 3, 6, 10, 12)
        [-4, 10, 3, 7, 15] -> 4 (-4, 3, 7, 15)
    """
    dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
    return _longest_increasing_subsequence_topdown(nums, 0, -1, dp)


def _longest_increasing_subsequence_topdown(
        nums: list[int], current_index: int, previous_index: int, dp: list[list[int]]) -> int:
    if current_index >= len(nums):
        return 0  # We at least have 1 number in our sequence

    if dp[current_index][previous_index] == -1:

        with_this_index = 0
        if previous_index == -1 or nums[current_index] > nums[previous_index]:
            with_this_index = 1 + _longest_increasing_subsequence(nums, current_index+1, current_index)

        skip_this_index = _longest_increasing_subsequence(nums, current_index+1, previous_index)

        dp[current_index][previous_index] = max(with_this_index, skip_this_index)

    return dp[current_index][previous_index]


def maximum_sum_increasing_subsequence(nums: list[int]) -> int:
    """
    Given a number sequence, find the increasing subsequence with the highest sum.
    Write a method that returns the highest sum.

    Example:
        [4, 1, 2, 6, 10, 1, 12] -> 32 (4, 6, 10, 12) [Note: 1, 2, 6, 10, 12 is longest, but not largest sum]
        [-4, 10, 3, 7, 15] -> 25 (10, 15) or (3, 7, 15)
    """
    return _maximum_sum_increasing_subsequence(nums, 0, -1)


def _maximum_sum_increasing_subsequence(nums: list[int], current_index: int, last_largest_index: int) -> int:
    """Recursive helper function."""
    if current_index >= len(nums):
        return 0

    sum_with_this_number = 0
    if last_largest_index == -1 or nums[current_index] > nums[last_largest_index]:
        sum_with_this_number = nums[current_index] + _maximum_sum_increasing_subsequence(nums, current_index+1, current_index)

    sum_without_this_number = _maximum_sum_increasing_subsequence(nums, current_index+1, last_largest_index)

    return max(sum_with_this_number, sum_without_this_number)


def maximum_sum_increasing_subsequence_topdown(nums: list[int]) -> int:
    """
    Given a number sequence, find the increasing subsequence with the highest sum.
    Write a method that returns the highest sum.

    Example:
        [4, 1, 2, 6, 10, 1, 12] -> 32 (4, 6, 10, 12) [Note: 1, 2, 6, 10, 12 is longest, but not largest sum]
        [-4, 10, 3, 7, 15] -> 25 (10, 15) or (3, 7, 15)
    """
    dp = [[math.inf for _ in range(len(nums))] for _ in range(len(nums))]
    return _maximum_sum_increasing_subsequence_topdown(nums, 0, -1, dp)


def _maximum_sum_increasing_subsequence_topdown(nums: list[int], current_index: int, last_largest_index: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if current_index >= len(nums):
        return 0

    if dp[current_index][last_largest_index] == math.inf:
        sum_with_this_number = 0
        if last_largest_index == -1 or nums[current_index] > nums[last_largest_index]:
            sum_with_this_number = nums[current_index] + _maximum_sum_increasing_subsequence_topdown(nums, current_index+1, current_index, dp)

        sum_without_this_number = _maximum_sum_increasing_subsequence_topdown(nums, current_index+1, last_largest_index, dp)

        dp[current_index][last_largest_index] = max(sum_with_this_number, sum_without_this_number)

    return dp[current_index][last_largest_index]


def shortest_common_supersequence(s1: str, s2: str) -> int:
    """
    Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest
    sequence which has ‘s1’ and ‘s2’ as subsequences.

    Example:
        s1=abcf, s2=bdcf -> 5 (abdcf)
        s1=dynamic, s2=programming -> 15 (dynprogrammicng)
    """
    # We need to produce a string that contains both other strings as subsequences
    # (actually just get the length of such a string)
    # Consider example 1: would abcdf be valid? I think so.
    # Looking at example 1, we know the common letters are bcf, each has 1 differing letter, which gives 5
    # Looking at example 2, common letters are amin(4). s1=7-4=3, s2=11-4=7==7+3+4=14?
    # dynamic - amin = dyc
    # Actually this doesn't work, because we have to worry about the order of the letters
    # If both chars are the same, skip them, otherwise try skipping one or the other and incrementing
    # s1=abc, s2=abc -> 3 (abc)
    return _shortest_common_supersequence(s1, s2, 0, 0)


def _shortest_common_supersequence(s1: str, s2: str, s1_index: int, s2_index: int) -> int:
    """Recursive helper function."""
    if s1_index >= len(s1):
        return len(s2)-s2_index

    if s2_index >= len(s2):
        return len(s1)-s1_index

    if s1[s1_index] == s2[s2_index]:
        return 1 + _shortest_common_supersequence(s1, s2, s1_index+1, s2_index+1)

    skip_s1 = 1 + _shortest_common_supersequence(s1, s2, s1_index+1, s2_index)
    skip_s2 = 1 + _shortest_common_supersequence(s1, s2, s1_index, s2_index+1)

    return min(skip_s1, skip_s2)


def shortest_common_supersequence_topdown(s1: str, s2: str) -> int:
    """
    Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest
    sequence which has ‘s1’ and ‘s2’ as subsequences.

    Example:
        s1=abcf, s2=bdcf -> 5 (abdcf)
        s1=dynamic, s2=programming -> 15 (dynprogrammicng)
    """
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return _shortest_common_supersequence_topdown(s1, s2, 0, 0, dp)


def _shortest_common_supersequence_topdown(s1: str, s2: str, s1_index: int, s2_index: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if s1_index >= len(s1):
        return len(s2)-s2_index

    if s2_index >= len(s2):
        return len(s1)-s1_index

    if dp[s1_index][s2_index] == -1:
        if s1[s1_index] == s2[s2_index]:
            dp[s1_index][s2_index] = 1 + _shortest_common_supersequence_topdown(s1, s2, s1_index+1, s2_index+1, dp)
        else:
            skip_s1 = 1 + _shortest_common_supersequence_topdown(s1, s2, s1_index+1, s2_index, dp)
            skip_s2 = 1 + _shortest_common_supersequence_topdown(s1, s2, s1_index, s2_index+1, dp)

            dp[s1_index][s2_index] = min(skip_s1, skip_s2)

    return dp[s1_index][s2_index]


def minimum_deletions_to_sort(nums: list[int]) -> int:
    """
    Given a number sequence, find the minimum number of elements that should be
    deleted to make the remaining sequence sorted.

    Example:
        [4, 2, 3, 6, 10, 1, 12] -> 2 (delete [4, 1])
        [-4, 10, 3, 7, 15] -> 1 (delete 10)
        [3, 2, 1, 0] -> 3 (only 1 element sorted)
        [2, 1, 3, 5] -> 1 (delete 1)
    """
    # At each stage, when it's unsorted, we can either try to keep this element
    # or skip this element and keep the next element
    # An easier solution is to take the len-len(longest increasing subsequence)
    longest_increasing_subseq = _minimum_deletions_to_sort(nums, 0, -1)
    return len(nums) - longest_increasing_subseq


def _minimum_deletions_to_sort(nums: list[int], index: int, last_largest_index: int) -> int:
    """Recursive helper function. (gets longest increasing subsequence)"""
    if index >= len(nums):
        return 0  # A single element is sorted

    with_this_index = 0
    if last_largest_index == -1 or nums[index] >= nums[last_largest_index]:
        with_this_index = 1 + _minimum_deletions_to_sort(nums, index+1, index)

    # Delete this index and take the next
    without_this_index = _minimum_deletions_to_sort(nums, index+1, last_largest_index)

    return max(with_this_index, without_this_index)


def minimum_deletions_to_sort_topdown(nums: list[int]) -> int:
    """
    Given a number sequence, find the minimum number of elements that should be
    deleted to make the remaining sequence sorted.

    Example:
        [4, 2, 3, 6, 10, 1, 12] -> 2 (delete [4, 1])
        [-4, 10, 3, 7, 15] -> 1 (delete 10)
        [3, 2, 1, 0] -> 3 (only 1 element sorted)
        [2, 1, 3, 5] -> 1 (delete 1)
    """
    # At each stage, when it's unsorted, we can either try to keep this element
    # or skip this element and keep the next element
    # An easier solution is to take the len-len(longest increasing subsequence)
    dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
    longest_increasing_subseq = _minimum_deletions_to_sort_topdown(nums, 0, -1, dp)
    return len(nums) - longest_increasing_subseq


def _minimum_deletions_to_sort_topdown(nums: list[int], index: int, last_largest_index: int, dp: list[list[int]]) -> int:
    """Recursive helper function. (gets longest increasing subsequence)"""
    if index >= len(nums):
        return 0  # A single element is sorted

    if dp[index][last_largest_index] == -1:
        with_this_index = 0
        if last_largest_index == -1 or nums[index] >= nums[last_largest_index]:
            with_this_index = 1 + _minimum_deletions_to_sort_topdown(nums, index+1, index, dp)

        # Delete this index and take the next
        without_this_index = _minimum_deletions_to_sort_topdown(nums, index+1, last_largest_index, dp)

        dp[index][last_largest_index] = max(with_this_index, without_this_index)

    return dp[index][last_largest_index]


def longest_repeating_subseq(s: str) -> int:
    """
    Given a sequence, find the length of its longest repeating subsequence (LRS).
    A repeating subsequence will be the one that appears at least twice in the
    original sequence and is not overlapping (i.e. none of the corresponding
    characters in the repeating subsequences have the same index).

    Example:
        tomorrow -> 2 (or, or)
        aabdbcec -> 3 (abc)
        fmff -> 2 (ff) -- note second f appears in 2 positions in different sequences
    """
    # Solution: If chars match, we can try recursing with 1 + next char
    # We can also try recursing skipping this char
    return _longest_repeating_subseq(s, 0, 0)


def _longest_repeating_subseq(s: str, index_1: int, index_2: int) -> int:
    """Recursive helper function."""
    if index_1 >= len(s) or index_2 >= len(s):
        return 0

    if index_1 != index_2 and s[index_1] == s[index_2]:
        return 1 + _longest_repeating_subseq(s, index_1+1, index_2+1)

    skip_index_1 = _longest_repeating_subseq(s, index_1+1, index_2)
    skip_index_2 = _longest_repeating_subseq(s, index_1, index_2+1)

    return max(skip_index_1, skip_index_2)


def longest_repeating_subseq_topdown(s: str) -> int:
    """
    Given a sequence, find the length of its longest repeating subsequence (LRS).
    A repeating subsequence will be the one that appears at least twice in the
    original sequence and is not overlapping (i.e. none of the corresponding
    characters in the repeating subsequences have the same index).

    Example:
        tomorrow -> 2 (or, or)
        aabdbcec -> 3 (abc)
        fmff -> 2 (ff) -- note second f appears in 2 positions in different sequences
    """
    # Solution: If chars match, we can try recursing with 1 + next char
    # We can also try recursing skipping this char
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    return _longest_repeating_subseq_topdown(s, 0, 0, dp)


def _longest_repeating_subseq_topdown(s: str, index_1: int, index_2: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if index_1 >= len(s) or index_2 >= len(s):
        return 0

    if dp[index_1][index_2] == -1:
        if index_1 != index_2 and s[index_1] == s[index_2]:
            dp[index_1][index_1] = 1 + _longest_repeating_subseq(s, index_1+1, index_2+1)
        else:
            skip_index_1 = _longest_repeating_subseq(s, index_1+1, index_2)
            skip_index_2 = _longest_repeating_subseq(s, index_1, index_2+1)

            dp[index_1][index_2] = max(skip_index_1, skip_index_2)

    return dp[index_1][index_2]


def subsequence_pattern_matching(s: str, pattern: str) -> int:
    """
    Given a string and a pattern, write a method to count the number of
    times the pattern appears in the string as a subsequence.

    Example:
        baxmx, ax -> 2 (bAXmx, bAxmX)
        tomorrow, tor -> 4 (TOmoRrow, TomORrow, TOmorRow, TomOrRow)
    """
    # store s index and last pattern index
    # if the indices match, recurse skipping the pattern index
    # and not skipping it
    # If we hit the end of pattern index, return 1
    return _subsequence_pattern_matching(s, pattern, 0, 0)


def _subsequence_pattern_matching(s: str, pattern: str, s_index: int, pattern_index: int) -> int:
    """Recursive helper function."""
    if pattern_index >= len(pattern):
        return 1

    if s_index >= len(s):
        return 0

    count = 0
    if s[s_index] == pattern[pattern_index]:
        count += _subsequence_pattern_matching(s, pattern, s_index+1, pattern_index+1)

    count += _subsequence_pattern_matching(s, pattern, s_index+1, pattern_index)

    return count


def subsequence_pattern_matching_topdown(s: str, pattern: str) -> int:
    """
    Given a string and a pattern, write a method to count the number of
    times the pattern appears in the string as a subsequence.

    Example:
        baxmx, ax -> 2 (bAXmx, bAxmX)
        tomorrow, tor -> 4 (TOmoRrow, TomORrow, TOmorRow, TomOrRow)
    """
    # store s index and last pattern index
    # if the indices match, recurse skipping the pattern index
    # and not skipping it
    # If we hit the end of pattern index, return 1
    dp = [[-1 for _ in range(len(pattern))] for _ in range(len(s))]
    return _subsequence_pattern_matching_topdown(s, pattern, 0, 0, dp)


def _subsequence_pattern_matching_topdown(s: str, pattern: str, s_index: int, pattern_index: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if pattern_index >= len(pattern):
        return 1

    if s_index >= len(s):
        return 0

    if dp[s_index][pattern_index] == -1:
        count = 0
        if s[s_index] == pattern[pattern_index]:
            count += _subsequence_pattern_matching_topdown(s, pattern, s_index+1, pattern_index+1, dp)

        count += _subsequence_pattern_matching_topdown(s, pattern, s_index+1, pattern_index, dp)
        dp[s_index][pattern_index] = count

    return dp[s_index][pattern_index]


def longest_bitonic_subsequence(nums: list[int]) -> int:
    """
    Given a number sequence, find the length of its Longest Bitonic
    Subsequence (LBS). A subsequence is considered Bitonic if it is
    monotonically increasing and then monotonically decreasing.

    Example:
        [4, 2, 3, 6, 10, 1, 12] -> 5 (2, 3, 6, 10, 12)
        [4, 2, 5, 9, 7, 6, 10, 3, 1] -> 7 (4, 5, 9, 7, 6, 10, 3, 1]

    # Skipping this one...but basically we need to check for the longest increasing / decreasing
    # sequence from each index, add them together and take the max len.
    """
    # For each index, if it's bigger than previous index, 1 + recurse
    # Then also recurse skipping that index
    return _longest_bitonic_subsequence(nums, 0, -1)


def _longest_bitonic_subsequence(nums: list[int], current_index: int, last_smallest_index: int) -> int:
    """Recursive helper function."""
    if current_index >= len(nums):
        return 0

    with_this_index = 0
    if last_smallest_index == -1 or nums[current_index] > nums[last_smallest_index]:
        with_this_index = 1 + _longest_bitonic_subsequence(nums, current_index+1, current_index)

    without_this_index = _longest_bitonic_subsequence(nums, current_index+1, last_smallest_index)

    return max(with_this_index, without_this_index)


def longest_alternating_sequence(nums: list[int]) -> int:
    """
    Given a number sequence, find the length of its Longest Alternating Subsequence (LAS).
    A subsequence is considered alternating if its elements are in alternating order.

    Example:
        [1, 2, 3, 4] -> 2 (1,2), (3,4), (1,3), (1,4)
        [3, 2, 1, 4] -> 3 (3,2,4), (2,1,4)
        [1, 3, 2, 4] -> 4 (1,3,2,4)
    """
    # From each index, we can take the next one if it's > or < than
    return _longest_alternating_sequence(nums, 0, -1, -1)


def _longest_alternating_sequence(nums: list[int], index: int, last_index: int, last_last_index: int) -> int:
    """Recursive helper function."""
    if index >= len(nums):
        return 0

    # Think of 1, 2, 3
    # When we get to 2, it has to be larger or smaller than 1
    # when we get to 3 it must be smaller than 2 since 1 was smaller

    with_this_index = 0
    if last_index == -1 or (nums[index] > nums[last_index] or nums[index] < nums[last_index]):
        # If last was larger, we need it to be smaller next and vice-versa
        if last_last_index == -1:
            with_this_index = 1 + _longest_alternating_sequence(nums, index+1, index, last_index)
        else:
            # 1, 2, 3
            if nums[last_index] > nums[last_last_index] and nums[index] < nums[last_index]:
                with_this_index = 1 + _longest_alternating_sequence(nums, index+1, index, last_index)
            # 3, 2, 1
            elif nums[last_index] < nums[last_last_index] and nums[index] > nums[last_index]:
                with_this_index = 1 + _longest_alternating_sequence(nums, index+1, index, last_index)

    without_this_index = _longest_alternating_sequence(nums, index+1, last_index, last_last_index)

    return max(with_this_index, without_this_index)


def longest_alternating_sequence_topdown(nums: list[int]) -> int:
    """
    Given a number sequence, find the length of its Longest Alternating Subsequence (LAS).
    A subsequence is considered alternating if its elements are in alternating order.

    Example:
        [1, 2, 3, 4] -> 2 (1,2), (3,4), (1,3), (1,4)
        [3, 2, 1, 4] -> 3 (3,2,4), (2,1,4)
        [1, 3, 2, 4] -> 4 (1,3,2,4)
    """
    # From each index, we can take the next one if it's > or < than
    dp = [[[-1 for _ in range(len(nums))] for _ in range(len(nums))] for _ in range(len(nums))]
    return _longest_alternating_sequence_topdown(nums, 0, -1, -1, dp)


def _longest_alternating_sequence_topdown(nums: list[int], index: int, last_index: int, last_last_index: int, dp: list[list[list[int]]]) -> int:
    """Recursive helper function."""
    if index >= len(nums):
        return 0

    # Think of 1, 2, 3
    # When we get to 2, it has to be larger or smaller than 1
    # when we get to 3 it must be smaller than 2 since 1 was smaller

    if dp[index][last_index][last_last_index] == -1:
        with_this_index = 0
        if last_index == -1 or (nums[index] > nums[last_index] or nums[index] < nums[last_index]):
            # If last was larger, we need it to be smaller next and vice-versa
            if last_last_index == -1:
                with_this_index = 1 + _longest_alternating_sequence_topdown(nums, index+1, index, last_index, dp)
            else:
                # 1, 2, 3
                if nums[last_index] > nums[last_last_index] and nums[index] < nums[last_index]:
                    with_this_index = 1 + _longest_alternating_sequence_topdown(nums, index+1, index, last_index, dp)
                # 3, 2, 1
                elif nums[last_index] < nums[last_last_index] and nums[index] > nums[last_index]:
                    with_this_index = 1 + _longest_alternating_sequence_topdown(nums, index+1, index, last_index, dp)

        without_this_index = _longest_alternating_sequence_topdown(nums, index+1, last_index, last_last_index, dp)

        dp[index][last_index][last_last_index] = max(with_this_index, without_this_index)

    return dp[index][last_index][last_last_index]


def edit_distance(s1: str, s2: str) -> int:
    """
    Given strings s1 and s2, we need to transform s1 into s2 by deleting, inserting, or
    replacing characters. Write a function to calculate the count of the minimum number of
    edit operations.

    Example:
        s1=bat, s2=but -> 1 (replace a with u)
        s1=abdca, s2=cdba -> 2 (replace a with c, and delete the second c)
        s1=passpot, s2=ppsspqrt -> 3 (replace a with p, replace q with o, delete/insert r)
    """
    # Imagine there are 2 pointers: s1 & s2, can we brute force try every operation?
    # If chars match, move on, otherwise try deletion, insertion or replacement
    # can insertion/deletion always be the same?
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return _edit_distance(s1, s2, 0, 0, dp)


def _edit_distance(s1: str, s2: str, s1_index: int, s2_index: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if s1_index >= len(s1):
        return len(s2)-s2_index  # Reached end of s1, need to insert chars for s2

    if s2_index >= len(s2):
        return len(s1) - s1_index  # Reached end of s2, need to insert chars for s1

    if dp[s1_index][s2_index] == -1:
        if s1[s1_index] == s2[s2_index]:
            dp[s1_index][s2_index] = _edit_distance(s1, s2, s1_index+1, s2_index+1, dp)  # Strings match
        else:
            # Deletion: Delete from s1
            deletion = 1 + _edit_distance(s1, s2, s1_index+1, s2_index, dp)
            # Insertion: Assume we insert something into s1
            insertion = 1 + _edit_distance(s1, s2, s1_index, s2_index+1, dp)
            # Replacement: Replace s1 with s2
            replacement = 1 + _edit_distance(s1, s2, s1_index+1, s2_index+1, dp)

            dp[s1_index][s2_index] = min(deletion, insertion, replacement)

    return dp[s1_index][s2_index]


def string_interleaving(m: str, n: str, p: str) -> bool:
    """
    Given three strings ‘m’, ‘n’, and ‘p’, write a method to find out if ‘p’ has been
    formed by interleaving ‘m’ and ‘n’. ‘p’ would be considered interleaving ‘m’ and
    ‘n’ if it contains all the letters from ‘m’ and ‘n’ and the order of letters is
    preserved too.

    Example:
        m=abd, n=cef, p=abcdef -> True (p contains all letters and matches the order)
        m=abd, n=cef, p=adcbef -> False (contains all letters but does not preserve order)
        m=abc, n=def, p=abdccf -> False (does not contain all letters)
        m=abcdef, n=mnop, p=mnaobcdepf -> True (contains all letters and in order)
        m=bb, n=bc, p=bbbc -> False (does not contain all the letters)
    """
    return _string_interleaving(m, n, p, 0, 0, 0)


def _string_interleaving(m: str, n: str, p: str, m_index: int, n_index: int, p_index: int) -> bool:
    """Recursive helper function."""
    if m_index == len(m) and n_index == len(n) and p_index == len(p):
        return True

    if m_index == len(m) and n_index == len(n) and p_index < len(p):
        return False  # end of m and n but p still has characters

    if m_index < len(m) and m[m_index] == p[p_index]:
        return _string_interleaving(m, n, p, m_index+1, n_index, p_index+1)

    if n_index < len(n) and n[n_index] == p[p_index]:
        return _string_interleaving(m, n, p, m_index, n_index+1, p_index+1)

    # No char could be matched
    return False
