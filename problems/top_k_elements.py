import heapq
from typing import List
from collections import Counter


def top_k_numbers(nums: List[int], k: int) -> List[int]:
    """
    Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

    [3, 1, 5, 12, 2, 11], k=3 -> [5, 12, 11]
    [5, 12, 11, -1, 12], k=3 -> [12, 11, 12]

    Time: O(n log k)
    Space: O(k)
    """
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap


def k_smallest_number(nums: List[int], k: int) -> int:
    """
    Given an unsorted array of numbers, find Kth smallest number in it.

    Please note that it is the Kth smallest number in the sorted order,
    not the Kth distinct element.

    [1, 5, 12, 2, 11, 5], k=3 -> 5 (1, 2, 5, 5, 11, 12)
    [1, 5, 12, 2, 11, 5], k=4 -> 5 (1, 2, 5, 5, 11, 12)
    [5, 12, 11, -1, 12], k=3 -> 11 (-1, 5, 11, 12, 12
    """
    # Solution: Use a max heap to keep track of the smallest k numbers.
    # If the size of the heap > k, remove the largest number.
    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return -max_heap[0]


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Given an array of points in a 2D plane, find ‘K’ closest points to the origin.

    [[1, 2], [1, 3]], k=1 -> [[1, 2]]
    [[1, 3], [3, 4], [2, -1]], k=2 -> [[1, 3], [2, -1]]
    """
    # Solution: We use a max heap again, but key it on square root
    max_heap = []

    for point in points:
        distance = point[0]**2 + point[1]**2
        heapq.heappush(max_heap, (-distance, point))

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [point[1] for point in max_heap]


def connect_ropes(costs: List[int]) -> int:
    """
    Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope
    with minimum cost. The cost of connecting two ropes is equal to the sum of their lengths.

    [1, 3, 11, 5] -> 33 (1+3)=4, +5(=9), +11(=20), 4+9+20 = 33
    """
    # Min cost will be when we take the two lowest numbers, so...
    # While heap...
    # take 2 smallest numbers, add them, put them back on, store the cost
    total_cost = []
    min_heap = []

    for cost in costs:
        heapq.heappush(min_heap, cost)

    while min_heap:
        cost_1 = heapq.heappop(min_heap)
        cost_2 = heapq.heappop(min_heap)
        cost_sum = cost_1 + cost_2
        total_cost.append(cost_sum)

        if min_heap:
            heapq.heappush(min_heap, cost_sum)

    return sum(total_cost)


def top_k_frequent_numbers(nums: List[int], k: int) -> List[int]:
    """
    Given an unsorted array of numbers, find the top ‘K’ frequently
    occurring numbers in it.

    [1, 3, 5, 12, 11, 12, 11], k=2 -> [12, 11]
    [5, 12, 11, 3, 11], k=2 -> [11, 5] or [11, 12] or [11, 3]
    """
    counts = Counter(nums)
    min_heap = []

    for num, count in counts.items():
        heapq.heappush(min_heap, (count, num))

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [elem[1] for elem in min_heap]


def frequency_sort(input: str) -> str:
    """
    Given a string, sort it based on the decreasing frequency of its characters.

    Programming -> rrggmmPiano
    abcbab -> bbbaac
    """
    max_heap = []
    output = []

    counts = Counter(input)

    # O(n log k), where k is distinct letter
    for letter, count in counts.items():
        heapq.heappush(max_heap, (-count, letter))

    while max_heap:
        count, letter = heapq.heappop(max_heap)
        count = count*-1
        for i in range(count):
            output.append(letter)

    return ''.join(output)


class KthLargestNumber:
    """
    Design a class to efficiently find the Kth largest element in a stream of numbers.

    The class should have the following two things:

    The constructor of the class should accept an integer array containing initial numbers
    from the stream and an integer ‘K’.
    The class should expose a function add(int num) which will store the given number and
    return the Kth largest number.

    Input: [3, 1, 5, 12, 2, 11], K=4
    - add(6) -> 5
    - add(13) -> 6
    - add(4) -> 6
    """
    # [1, 2, 3, 5, 11, 12] >
    # [1, 2, 3, 5, 6, 11, 12] > 5
    # [1, 2, 3, 5, 6, 11, 12, 13] > 6
    # [1, 2, 3, 4, 5, 6, 12, 13] > 6
    def __init__(self, nums: List[int], k: int) -> None:
        self._min_heap = []
        self._k = k

        for num in nums:
            heapq.heappush(self._min_heap, num)

            if len(self._min_heap) > self._k:
                heapq.heappop(self._min_heap)

    def add(self, num: int) -> int:
        heapq.heappush(self._min_heap, num)

        if len(self._min_heap) > self._k:
            heapq.heappop(self._min_heap)

        return self._min_heap[0]


def k_closest_numbers(nums: List[int], k: int, x: int) -> List[int]:
    """
    Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’
    in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in
    the array.

    [5, 6, 7, 8, 9], k=3, x=7 -> [6, 7, 8]
    [2, 4, 5, 6, 9], k=3, x=6 -> [4, 5, 6]
    [2, 4, 5, 6, 9], k=3, x=10 -> [5, 6, 9]
    """
    # We could also use 2 points and a deque to solve this.

    # Find the number closest to X (log n)
    closest_index = _bfs(nums, x)

    # get the range of possible closest numbers
    left_range = closest_index-k
    highest_range = closest_index+k
    left_range = max(left_range, 0)
    highest_range = min(highest_range, len(nums)-1)

    # Push those numbers onto the min heap
    min_heap = []

    # k log k
    for i in range(left_range, highest_range+1):
        heapq.heappush(min_heap, (abs(nums[i]-x), nums[i]))

    # k log k
    result = []
    for i in range(k):
        result.append(heapq.heappop(min_heap)[1])

    result.sort()
    return result


def _bfs(nums: List[int], key: int) -> int:
    """Helper to find the element closest to index."""
    # [1, 5, 7, 9, 10], key=6
    #     ^
    #     ^
    #     ^
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == key:
            return mid
        elif key > nums[mid]:
            left = mid+1
        else:
            right = mid-1

    if left > 0:
        return left-1

    return left


def max_distinct_numbers(nums: List[int], k: int) -> int:
    """
    Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from
    the array such that we are left with maximum distinct numbers.

    [7, 3, 5, 8, 5, 3, 3], k=2 -> 3
        (remove 2 3's and be left with 3 distinct numbers [7, 3, 8] -- 5 is skipped because it occurs twice)
        ([7, 5, 8] would also be a solution -- remove one 5 and one 3)
    [3, 5, 12, 11, 12], k=3 -> 2
        (remove one 12 to make that distinct, then remove 2 other numbers)
    [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], k=2 -> 3
        (remove a 4 to get 3 distinct numbers)
    """
    # {3: 3, 5: 2, 7: 1, 8: 1}
    # We get the counts of each number
    # For each number with a 1 count, we'll put it on a distinct set
    # Otherwise, let's put the counts in a min heap, keyed on the repeat count
    # While we have k, make it unique, add to unique set
    # Finally, if we have done that and we STILL have k, remove from unique set and
    #   return the size of that set
    counts = Counter(nums)
    unique_nums = set()
    min_heap = []

    # {3: 3, 5: 2, 7: 1, 8: 1}
    # unique_nums: (7, 8, 5)
    # heap: [(3, 3)]
    # k=-1
    #

    for num, count in counts.items():
        if count == 1:
            # Distinct number, we want to try and preserve it
            unique_nums.add(num)
        else:
            # Add the duplicate numbers to the min_heap
            heapq.heappush(min_heap, (count, num))

    # Now, we want to try and remove the dupe numbers to make them unique
    while min_heap and k > 0:
        count, num = heapq.heappop(min_heap)
        diff = abs(1-count)
        if diff <= k:
            # We can reduce it to 1
            unique_nums.add(num)
        k -= diff

    result = len(unique_nums)

    if k > 0:
        result -= k

    return result


def sum_of_elements(nums: List[int], k1: int, k2: int) -> int:
    """
    Given an array, find the sum of all numbers between the K1’th and K2’th
    smallest elements of that array.

    [1, 3, 12, 5, 15, 11], k1=3, k2=6 -> 23
        ([1, 3, 5, 11, 12, 15], k1=5, k2=6 (11+12)=23
    [3, 5, 8, 7], k1=1, k2=4 -> 12
        ([3, 5, 7, 8], k1=3, k4=8 (5+7) = 12
    """
    # We have a min heap of size n-k1
    # Then we pop it k2-k1-1 times
    # O(n log n-k1) + O(k2-k1)
    max_heap_size = len(nums)-k1
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > max_heap_size:
            heapq.heappop(min_heap)

    heap_sum = 0
    for _ in range(k2-k1-1):
        heap_sum += heapq.heappop(min_heap)

    return heap_sum


def rearrange_string(input: str) -> str:
    """
    Given a string, find if its letters can be rearranged in such a way that no two
    same characters come next to each other.

    aappp -> papap
    Programming -> rgmrgmPiano or "gmringmrPoa" or "gmrPagimnor", etc.
    aapa -> "" (2 a's will always come next to each other)
    """
    # Take a max heap keyed on the char counts.
    # {p: 3, a: 2}
    # Pop the letter, add it to the string.
    # If count is 0, ignore, else Save it {last = p, {a: 2}
    # If heap is empty, break -- if our new string matches input len we're done
    # Else, add on the next biggest letter, pop on the old letter
    max_heap = []
    counts = Counter(input)

    for letter, count in counts.items():
        heapq.heappush(max_heap, (-count, letter))

    output = []
    last_letter = None
    last_count = 0

    while max_heap:
        count, letter = heapq.heappop(max_heap)
        count *= -1
        output.append(letter)
        count -= 1

        if last_letter:
            heapq.heappush(max_heap, (-last_count, last_letter))

        if count > 0:
            last_letter = letter
            last_count = count
        else:
            last_letter = None

    if len(output) == len(input):
        return ''.join(output)

    return ''
