import heapq
from collections import Counter
from typing import List


def top_k_frequent(items: List[int], k: int) -> List[int]:
    """Given a list of items, return the top k occuring items.

    Example: [1, 1, 1, 2, 2, 3], k=2 -> [1, 2]

    1. Get the counts of each item
    2. Put the counts in a heap, popping the min if over a certain size
    3. Now return the elements from the heap

    Note: For most frequent, we use a min heap (get rid of smallest)
          For least frequent, we use a max heap (get rid of largest)

    Time:  O(n log k)
    Space: O(n+k)
    """
    if k == len(items):
        return items

    counts = Counter(items)

    heap = []

    for item, frequency in counts.items():
        heapq.heappush(heap, (frequency, item))
        if len(heap) > k:
            heapq.heappop(heap)

    return [element[1] for element in heap]
