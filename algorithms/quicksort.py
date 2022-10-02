from typing import Any, List


def quicksort(items: List[Any]) -> None:
    """A quicksort implementation.

    * While left < right
    * Partition the array
    * Recursively sort the left half
    * Recursively sort the right half

    Time: O(n log n) - average
          O(n^2) - worst, happens when pivot max/min in sorted array.
                    Can avoid be shuffling.

    Space: O(n log n)

    NOT stable.
    """
    _quicksort(items, 0, len(items)-1)


def _quicksort(items: List[Any], left: int, right: int) -> None:
    """Recursive helper function.

    Partition
    * Get the pivot in the correct position via partition.
    * Sort to the left of the pivot.
    * Sort to the right of the pivot.
    """
    if left < right:
        pivot_index = _partition(items, left, right)

        _quicksort(items, left, pivot_index-1)
        _quicksort(items, pivot_index+1, right)


def _partition(items: List[Any], left: int, right: int) -> int:
    """Partitions the array around the pivot value.

    Picks a pivot value and sorts everything to the left <= pivot,
    and everything greater than the pivot to the right.

    At the end, the pivot will be in the correct position.

    Ex. [100, 5, -2, 1, 52, 3, 4]
        [-2, 5, 100, 1, 52, 3, 4]
        [-2, 1, 100, 5, 52, 3, 4]
        [-2, 1, 3, 5, 52, 100, 4]
        [-2, 1, 3, 4, 52, 100, 5]

    1. Pick a pivot value (rightmost pos)
    2. Set a pointer i to the left -- i represents biggest element
    3. Iterate until the pivot:
        * If we find an element <= pivot
        * Swap it with i
        * Increment i
    4. Swap the pivot with i
    5. Return the pivot position
    """
    # Choose rightmost element as the pivot
    pivot_val = items[right]

    # Greater element pointer.
    # We know the pointer must point to something greater than the pivot,
    # because otherwise if not it would have been swapped.
    i = left

    for j in range(left, right):
        if items[j] <= pivot_val:
            # An item <= pivot was found, swap it
            items[i], items[j] = items[j], items[i]
            i += 1

    # Swap the pivot item with the greater element
    items[i], items[right] = items[right], items[i]

    # Return position where the partition finished
    return i
