from typing import Any, List


def mergesort(items: List[Any]) -> List[Any]:
    """A merge sort implementation.

    Steps:
    * If len <= 1, return
    * Get the mid
    * Merge sort the 2 halves recursively
    * Merge the two halves
        - Take the smaller item until index hits an end
        - Fill up with the remaining items

    Use for sorting linked lists.
    Use if all the data can't fit into memory.

    Time: O(n log n)
    Space: O(n), for auxiliary arrays
    Stable: Yes.
    """
    if len(items) <= 1:
        return items

    mid = len(items) // 2

    left = mergesort(items[:mid])
    right = mergesort(items[mid:])

    return _merge(left, right)


def _merge(left: List[Any], right: List[Any]) -> List[Any]:
    """Merges two arrays into one.

    * Set up 2 points and merged array.
    * Take the lowest element from both arrays, copy it over
    * Copy the remaining elements form either array
    """
    i = 0
    j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged
