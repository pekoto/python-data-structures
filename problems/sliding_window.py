from collections import Counter
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


def k_distinct_chars(items: str, k: int) -> int:
    """
    Given a string, find the length of the longest substring in it with no more
    than K distinct characters.

    You can assume that K is less than or equal to the length of the given string.

    Example 1:

    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".
    """
    counts = {}
    max_len = 0
    start = 0
    distinct_chars = 0

    for end in range(len(items)):
        c = items[end]

        if c not in counts or counts[c] == 0:
            counts[c] = 0
            distinct_chars += 1

        counts[c] += 1

        while distinct_chars > k:
            start_char = items[start]
            counts[start_char] -= 1
            if counts[start_char] == 0:
                distinct_chars -= 1
            start += 1

        max_len = max(max_len, (end - start) + 1)

    return max_len


def longest_substring_with_distinct_chars(input_str: str) -> int:
    """
    Given a string, find the length of the longest substring, which has all distinct characters.

    Example 1:
    Input: String="aabccbb", Output: 3
    Explanation: The longest substring with distinct characters is "abc".
    """
    max_len = 0
    start = 0
    char_counts = {}
    repeated_chars = 0

    for end in range(len(input_str)):
        c = input_str[end]

        if c not in char_counts:
            char_counts[c] = 0

        if char_counts[c] >= 1:
            repeated_chars += 1

        char_counts[c] += 1

        while repeated_chars > 0:
            start_char = input_str[start]
            if char_counts[start_char] == 2:
                repeated_chars -= 1
            char_counts[start_char] -= 1
            start += 1

        max_len = max(max_len, (end-start)+1)

    return max_len


def longest_substring_with_letter_replacement(input_str: str, k: int) -> int:
    """
    Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

    Example 1:

    Input: String="aabccbb", k=2
    Output: 5
    Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
    """
    most_frequent_char_count = 0  # Represents char that is the same.
    char_counts = {}
    max_len = 0
    start = 0

    for end in range(len(input_str)):
        c = input_str[end]

        if c not in char_counts:
            char_counts[c] = 0

        char_counts[c] += 1

        # Check if this char is the most common char.
        # We want to replace all of the other chars.
        most_frequent_char_count = max(most_frequent_char_count, char_counts[c])

        # Check if the window size - most frequent char is > k.
        # All of the chars that are not the most frequent need to be replaced.
        if (((end-start)+1) - most_frequent_char_count) > k:
            start_char = input_str[start]
            char_counts[start_char] -= 1
            start += 1
            # Why not update most frequent char?
            # Well, max_len would not be updated, since we just shrunk the window,
            # and most_frequent would get updated in the next iteration anyway.

        max_len = max(max_len, (end-start)+1)

    return max_len


def longest_substring_with_one_replacement(input_arr: List[int], k: int) -> int:
    """
    Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

    Example 1:

    Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
    Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
    """
    start = 0
    max_len = 0
    replacement_count = 0

    for end in range(len(input_arr)):
        if input_arr[end] == 0:
            replacement_count += 1

        while replacement_count > k:
            if input_arr[start] == 0:
                replacement_count -= 1

            start += 1

        max_len = max(max_len, (end-start)+1)

    return max_len


def str_contains_permutation(input_str: str, pattern: str) -> bool:
    """
    Given a string and a pattern, find out if the string contains any permutation of the pattern.
    Input: String="oidbcaf", Pattern="abc"
    Output: true
    Explanation: The string contains "bca" which is a permutation of the given pattern.
    """
    pattern_counts = Counter(pattern)
    start = 0
    matched = 0

    for end in range(len(input_str)):
        c = input_str[end]

        if c in pattern_counts:
            pattern_counts[c] -= 1
            if pattern_counts[c] >= 0:
                matched += 1

        if matched == len(pattern):
            return True

        if end + 1 >= len(pattern):
            start_c = input_str[start]
            start += 1

            if start_c in pattern_counts:
                if pattern_counts[start_c] == 0:
                    matched -= 1
                pattern_counts[start_c] += 1

    return False


def anagram_indices(input_str: str, pattern: str) -> List[int]:
    """
    Given a string and a pattern, find all anagrams of the pattern in the given string.
    Input: String="ppqp", Pattern="pq"
                   ^
                   ^
    Output: [1, 2]
    """
    pattern_counts = Counter(pattern)
    start = 0
    matched = 0
    indices = []

    for end in range(len(input_str)):
        c = input_str[end]

        if c in pattern_counts:
            if pattern_counts[c] > 0:
                matched += 1
            pattern_counts[c] -= 1

        if matched == len(pattern):
            indices.append(start)

        if end + 1 >= len(pattern):
            start_c = input_str[start]
            if start_c in pattern_counts:
                if pattern_counts[start_c] == 0:
                    matched -= 1
                pattern_counts[start_c] += 1

            start += 1

    return indices


def smallest_substr_window(input_str: str, pattern: str) -> str:
    """
    Given a string and a pattern, find the smallest substring in the given string
    which has all the character occurrences of the given pattern.

    Input: String="abdbca", Pattern="abc"
    Output: "bca"
    Explanation: The smallest substring having all characters of the pattern is "bca".
    """
    start = 0
    matched = 0
    char_counts = Counter(pattern)
    start_index = -1
    end_index = len(input_str)+1

    for end in range(len(input_str)):
        c = input_str[end]

        if c in char_counts and char_counts[c] > 0:
            matched += 1

        char_counts[c] -= 1

        while matched == len(pattern):

            if (end - start) < (end_index-start_index):
                end_index = end
                start_index = start

            start_c = input_str[start]
            if start_c in char_counts:
                if char_counts[start_c] == 0:
                    matched -= 1
                char_counts[start_c] += 1
                start += 1

    if start_index == -1:
        return ""

    return input_str[start_index:end_index+1]


def word_concat(input_str: str, words: List[str]) -> List[int]:
    """
    Given a string and a list of words, find all the starting indices of substrings in the
    given string that are a concatenation of all the given words exactly once without any
    overlapping of words. It is given that all words are of the same length.

    Input: String="catfoxcat", Words=["cat", "fox"]
    Output: [0, 3]
    Explanation: The two substring containing both the words are "catfox" & "foxcat".

    Note: This solution covers all test cases but may be wrong as the question is ambiguous.
    """
    start = 0
    matched = 0
    word_counts = Counter(words)
    word_len = len(words[0])
    indices = []

    for end in range(0, len(input_str), word_len):
        substr = input_str[end:end+word_len]

        if word_counts[substr] > 0:
            matched += 1

        word_counts[substr] -= 1

        if ((end+word_len)-start) == word_len*len(words):
            if matched == len(words):
                indices.append(start)

            substr = input_str[start:start+word_len]

            if word_counts[substr] == 0:
                matched -= 1

            word_counts[substr] += 1
            start += word_len

    return indices
