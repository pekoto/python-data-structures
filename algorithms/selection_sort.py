from typing import List


def selection_sort(items: List[int]) -> None:
    """A selection sort implementation.

    Usually bad performance, BUT can be useful if you want to
    minimize writes and need an in-place algorithm.

    NOT stable.

    Time: O(n^2), O(n) swaps worst-case, O(1) swaps best-case
    Space: O(1) (in place)
    """
    for i in range(len(items)):
        min_elem = i

        # Finds the minimum element
        for j in range(i+1, len(items)):
            if items[j] < items[min_elem]:
                min_elem = j

        # If i was not the minimum element, swap it.
        if min_elem != i:
            items[i], items[min_elem] = items[min_elem], items[i]
