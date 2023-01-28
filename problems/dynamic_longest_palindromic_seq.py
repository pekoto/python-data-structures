def longest_palindromic_sequence(s: str) -> int:
    """
    Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
    In a palindromic subsequence, elements read the same backward and forward.

    A subsequence is a sequence that can be derived from another sequence by deleting
    some or no elements without changing the order of the remaining elements.

    Example 1:
    Input: "abdbca" -> 5 (LPS is "abdba")
    """
    return _longest_palindromic_sequence(s, 0, len(s)-1)


def _longest_palindromic_sequence(s: str, start: int, end: int) -> int:
    if start > end:
        return 0

    if start == end:  # 1 element sequence is a palindrome
        return 1

    if s[start] == s[end]:
        return 2 + _longest_palindromic_sequence(s, start+1, end-1)

    skip_start = _longest_palindromic_sequence(s, start+1, end)
    skip_end = _longest_palindromic_sequence(s, start, end-1)

    return max(skip_start, skip_end)


def longest_palindromic_sequence_topdown(s: str) -> int:
    """
    Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
    In a palindromic subsequence, elements read the same backward and forward.

    A subsequence is a sequence that can be derived from another sequence by deleting
    some or no elements without changing the order of the remaining elements.

    Example 1:
    Input: "abdbca" -> 5 (LPS is "abdba")
    Time / Space is O(n^2), since that is the size of our array / max number of unique subproblems.
    """
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    return _longest_palindromic_sequence_topdown(s, 0, len(s)-1, dp)


def _longest_palindromic_sequence_topdown(s: str, start: int, end: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if start > end:
        return 0

    if start == end:
        return 1

    if dp[start][end] == -1:
        if s[start] == s[end]:
            dp[start][end] = 2 + _longest_palindromic_sequence_topdown(s, start+1, end-1, dp)
        else:
            skip_start = _longest_palindromic_sequence_topdown(s, start+1, end, dp)
            skip_end = _longest_palindromic_sequence_topdown(s, start, end-1, dp)
            dp[start][end] = max(skip_start, skip_end)

    return dp[start][end]


def longest_palindromic_sequence_bottomup(s: str) -> int:
    """
    Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
    In a palindromic subsequence, elements read the same backward and forward.

    A subsequence is a sequence that can be derived from another sequence by deleting
    some or no elements without changing the order of the remaining elements.

    Example 1:
    Input: "abdbca" -> 5 (LPS is "abdba")
    """
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

    for i in range((len(s))):
        dp[i][i] = 1  # Every 1-letter element will be at least 1

    for start in range(len(s)-1, -1, -1):  # Go backwards from lower right
        for end in range(start+1, len(s)):
            if s[start] == s[end]:
                dp[start][end] = 2 + dp[start+1][end-1]
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1])

    return dp[0][len(s)-1]


def longest_palindromic_substr(s: str) -> int:
    """
    Given a string, find the length of its Longest Palindromic Substring (LPS). In
    a palindromic string, elements read the same backward and forward.

    Example: cddpd -> 3 (dpd)
    Time: O(3^n)
    """
    # Well, here is the recursive solution:
    # If the two chars match, then check the remaining chars
    # If we find the result matches the len(remaining chars), whole thing can be returned
    # Else return the max of skipping the first or second.
    return _longest_palindromic_substr(s, 0, len(s)-1)


def _longest_palindromic_substr(s: str, start: int, end: int) -> int:
    """Recursive helper function."""
    if start > end:
        return 0

    if start == end:
        return 1  # 1 element str is always a palindrome

    if s[start] == s[end]:
        remaining_chars = end-start-1
        result = _longest_palindromic_substr(s, start+1, end-1)
        if result == remaining_chars:
            return 2 + result

    skip_start = _longest_palindromic_substr(s, start+1, end)
    skip_end = _longest_palindromic_substr(s, start, end-1)

    return max(skip_start, skip_end)


def longest_palindromic_substr_topdown(s: str) -> int:
    """
    Given a string, find the length of its Longest Palindromic Substring (LPS). In
    a palindromic string, elements read the same backward and forward.

    Example: cddpd -> 3 (dpd)
    """
    # Well, here is the recursive solution:
    # If the two chars match, then check the remaining chars
    # If we find the result matches the len(remaining chars), whole thing can be returned
    # Else return the max of skipping the first or second.
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    return _longest_palindromic_substr_topdown(s, 0, len(s)-1, dp)


def _longest_palindromic_substr_topdown(s: str, start: int, end: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if start > end:
        return 0

    if start == end:
        return 1

    if dp[start][end] == -1:
        if s[start] == s[end]:
            remaining_chars = end-start-1
            result = _longest_palindromic_substr_topdown(s, start+1, end-1, dp)
            if result == remaining_chars:
                dp[start][end] = 2 + result
                return dp[start][end]

        skip_start = _longest_palindromic_substr_topdown(s, start+1, end, dp)
        skip_end = _longest_palindromic_substr_topdown(s, start, end-1, dp)

        dp[start][end] = max(skip_start, skip_end)

    return dp[start][end]


def count_palindromic_substr(s: str) -> int:
    """
    Given a string, find the total number of palindromic substrings in it. Please
    note we need to find the total number of substrings and not subsequences.

    Example:
        abdbca -> 7 (a, b, d, b, c, a, bdb)
    """
    # If we take the string bdb and split it to bd and db, the problem is the d in the middle would be counted twice
    # The trick is when we take the palindrome for the two substrs, we need to subtract the palindromes from the string
    # in-between, since those will have been double-counted.
    return _count_palindromic_substr(s, 0, len(s)-1)


def _count_palindromic_substr(s: str, start: int, end: int) -> int:
    """Recursive helper function."""
    if start > end:
        return 0

    if start == end:
        return 1  # Every len(1) str is a palindrome.

    count = 0
    if _is_palindromic(s, start, end):
        count += 1

    count += _count_palindromic_substr(s, start+1, end)
    count += _count_palindromic_substr(s, start, end-1)
    count -= _count_palindromic_substr(s, start+1, end-1)  # Subtract double-counted palindromes

    return count


def _is_palindromic(s: str, start: int, end: int) -> bool:
    """Recursive helper function."""
    while start <= end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True


def count_palindromic_substr_simple(s: str) -> int:
    """
    Given a string, find the total number of palindromic substrings in it. Please
    note we need to find the total number of substrings and not subsequences.

    Example:
        abdbca -> 7 (a, b, d, b, c, a, bdb)
    """
    count = len(s)  # Every 1-char str is a palindrome.

    for end in range(1, len(s)):
        for start in range(0, end):
            if _is_palindromic_simple(s, start, end):
                count += 1

    return count


def _is_palindromic_simple(s: str, start: int, end: int) -> bool:
    while start <= end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True


def minimum_deletions(s: str) -> int:
    """
    Given a string, find the minimum number of characters that we can remove to make
    it a palindrome.

    abdbca -> 1 (remove c to give abdba)
    cddpd -> 2 (remove c, d to give ddd)
    pqr -> 2 (remove any two to give a single char, p, q, or r)

    # Similar (Same approach can solve):
        "Minimum insertions to make a string palindroic"
        "Is a string palindromic if we make K insertions?"
    """
    # Observation: The num of chars would be total chars - longest palindromic seq
    return len(s) - _minimum_deletions(s, 0, len(s)-1)


def _minimum_deletions(s: str, start: int, end: int) -> int:
    """Recursive helper function."""
    if start > end:
        return 0

    if start == end:
        return 1   # len(1) char is palindromic

    if s[start] == s[end]:
        return 2 + _minimum_deletions(s, start+1, end-1)

    skip_start = _minimum_deletions(s, start+1, end)
    skip_end = _minimum_deletions(s, start, end-1)

    return max(skip_start, skip_end)


def minimum_deletions_topdown(s: str) -> int:
    """
    Given a string, find the minimum number of characters that we can remove to make
    it a palindrome.

    abdbca -> 1 (remove c to give abdba)
    cddpd -> 2 (remove c, d to give ddd)
    pqr -> 2 (remove any two to give a single char, p, q, or r)

    # Similar (Same approach can solve):
        "Find longest palindromic subsequence" (just don't do len(s)-"
        "Minimum insertions to make a string palindroic"
        "Is a string palindromic if we make K insertions?"
    """
    # Observation: The num of chars would be total chars - longest palindromic seq
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    return len(s) - _minimum_deletions_topdown(s, 0, len(s)-1, dp)


def _minimum_deletions_topdown(s: str, start: int, end: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if start > end:
        return 0

    if start == end:
        return 1   # len(1) char is palindromic

    if dp[start][end] == -1:

        if s[start] == s[end]:
            dp[start][end] = 2 + _minimum_deletions_topdown(s, start+1, end-1, dp)
        else:
            skip_start = _minimum_deletions_topdown(s, start+1, end, dp)
            skip_end = _minimum_deletions_topdown(s, start, end-1, dp)

            dp[start][end] = max(skip_start, skip_end)

    return dp[start][end]


def palindrome_partitioning(s: str) -> int:
    """
    Given a string, we want to cut it into pieces such that each piece is a
    palindrome. Write a function to return the minimum number of cuts needed.

    Example:
        abdbca -> 3 (a, bdb, c, a)
        cddpd -> 2 (c, d, dpd)
        pqr -> 2 (p, q, r)
        pp -> 0 (fully palindromic)
    """
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
    dp_palindrome = [[-1 for _ in range(len(s))] for _ in range(len(s))]

    return _palindrome_partitioning(s, 0, len(s)-1, dp, dp_palindrome)


def _palindrome_partitioning(s: str, start: int, end: int, dp: list[list[int]], dp_palindrome: list[list[int]]) -> int:
    """Recursive helper function."""
    if start > end:
        return 0

    if _is_palindromic_s(s, start, end):
        return 0  # No cuts needed if already a palindrome.

    if dp[start][end] == -1:
        count = end-start  # We need at max len(s)-1 cuts

        for i in range(start, end+1):
            if _is_palindromic_s(s, start, i):
                count = min(count, 1 + _palindrome_partitioning(s, i+1, end, dp, dp_palindrome))

        dp[start][end] = count

    return dp[start][end]


def _is_palindromic_s(s: str, start: int, end: int) -> bool:
    while start <= end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True
