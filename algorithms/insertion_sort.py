from typing import Any, List


def insertion_sort(items: List[Any]) -> None:
    """Insertion sort implementation.

    Insertion sort is not common, but can be good if the array is already sorted.

    Best case: O(n)
    Worst case: O(n^2) -- array reverse sorted.

    Stable.
    Space: O(1)

    1. Iterate around the array.
    2. While the item is < item-1, swap them.
    """
    for i in range(1, len(items)):
        j = i

        while j > 0 and items[j] < items[j-1]:
            # While j is smaller than j-1, swap them
            items[j-1], items[j] = items[j], items[j-1]
            j -= 1
