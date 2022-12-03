from typing import Any, List
import heapq

"""
Design a class to calculate the median of a number stream. The class should have the
following two methods:

    insertNum(int num): stores the number in the class
    findMedian(): returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will be the average
of the middle two numbers.

> insert(3)
> insert(1)
[1, 3] -> 2
> insert(5)
[1, 3, 5] -> 3
> insert(4)
[1, 3, 4, 5] -> 3.5
max_heap = [3, 1], min_heap = [4, 5]
"""


class NumberStreamMedian:
    """
    We will use 2 heaps:
    - max heap holds smallest numbers -> [1...x]
    - min heap holds larger numbers -> [y...100]

    Time: O(log n) for insert, O(1) for find median
    Space: O(n)
    """
    def __init__(self) -> None:
        self._min_heap = []
        self._max_heap = []

    def insert_num(self, num: int) -> None:
        if not self._max_heap or num <= -self._max_heap[0]:
            # Either the first half if empty,
            # or the number is <= the top of the max heap (store of min numbers)
            heapq.heappush(self._max_heap, -num)
        else:
            heapq.heappush(self._min_heap, num)

        # Now, we want to keep our heaps balance, or have 1 more element
        # in our max heap (list of smaller numbers).
        if len(self._max_heap) > len(self._min_heap) + 1:  # Can be 1 bigger
            # Move the max number to the min heap (second half, larger numbers)
            max_number = -heapq.heappop(self._max_heap)
            heapq.heappush(self._min_heap, max_number)
        elif len(self._max_heap) < len(self._min_heap):
            # Move the smallest number to min heap (first half, smaller numbers)
            min_number = -heapq.heappop(self._min_heap)
            heapq.heappush(self._max_heap, min_number)

    def find_median(self) -> float:
        if len(self._min_heap) != len(self._max_heap):
            return -self._max_heap[0]
        else:
            min_val = self._min_heap[0]
            max_val = -self._max_heap[0]

            return (min_val+max_val) / 2


def maximize_capital(capitals: List[int], profits: List[int], initial_capital: int, num_projects: int) -> int:
    """
    Given a set of investment projects with their respective profits, we need to find the most
    profitable projects. We are given an initial capital and are allowed to invest only in a
    fixed number of projects. Our goal is to choose projects that give us the maximum profit.
    Write a function that returns the maximum total capital after selecting the most profitable
    projects.

    We can start an investment project only when we have the required capital. Once a project is
    selected, we can assume that its profit has become our capital.

    Example:
    Input: Project Capitals=[0,1,2,3], Project Profits=[1,2,3,5],
           Initial Capital=0, Number of Projects=3
    Output: 8

    With ‘0’ capital, we can only select the first project, bringing out capital to 1.
    Next, we will select the second project, which will bring our capital to 3.
    Next, we will select the fourth project, giving us a profit of 5.

    After selecting the three projects, our total capital will be 8 (1+2+5).
    """
    # At each stage, we want to take the one with the most profit.
    # We iterate around capitals, adding profits to the heap as long as we have enough capital.
    # Increment the capital, start again.
    # Do this for num_projects time to get the total.
    # heap: [(1, 0)], capital: 1, profits = 1
    # heap: [(2, 1), (1,0)], capital 3 (capital += profit)
    # heap: [(5, 3), (3,2)], capital: 8 (capital += profit)
    # Actually, what we can do is put the capital on a min heap
    # Keep popping the min heap while we can do a project and put the profit on a max heap
    # Take the project from the max heap

    min_capital_heap = []
    max_profit_heap = []

    for i in range(len(capitals)):
        # Put capital in a min heap
        heapq.heappush(min_capital_heap, (capitals[i], i))

    available_capital = initial_capital

    for _ in range(num_projects):

        while min_capital_heap and min_capital_heap[0][0] <= available_capital:
            capital, i = heapq.heappop(min_capital_heap)
            heapq.heappush(max_profit_heap, -profits[i])

        if not max_profit_heap:
            break  # We can't do any projects

        available_capital += -heapq.heappop(max_profit_heap)

    return available_capital


def next_interval(intervals: List[List[int]]) -> List[int]:
    """
    Given an array of intervals, find the next interval of each interval.
    In a list of intervals, for an interval ‘i’ its next interval ‘j’ will
    have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

    Write a function to return an array containing indices of the next interval of
    each input interval. If there is no next interval of a given interval, return -1.
    It is given that none of the intervals have the same start point.

    Example:

    Input: Intervals [[3,4], [1,5], [4,6]]
    Output: [2, -1, -1]
    Explanation: The next interval of [3,4] is [4,6] which has index ‘2’.
    There is no next interval for [1,5] and [4,6].
    """
    # Brute force: Check for earliest start >= end of each interval O^2
    # Better? No: Sort, check for overlaps, and hold original index map --> however also becomes O^2
    # So let's think about using heaps.
    # For each interval, I want to find the closest start that comes >= end.
    # E.g. 3,4 > 4,6
    # max_start_heap: [4,6], [3,4], [1,5]
    # max_end_heap: [4,6], [1,5], [3,4]
    # For 4,6, None of the intervals match, as the top start is < end
    # [-1, -1, -1]
    # For 1,5, same deal -- 4<5, so skip it
    # for 3,4, 4,6 matches. So we set that.
    # We continue, but none of the rest match.
    # Because they are sorted in end times. Any we popped off would be too large for the following intervals.
    # max start: [5,6], [3,4], [2,3], [1,3]
    # max end: [5,6], [3,4], [2,3], [1,3]
    # 5,6 > skip it max start is before the end
    # 3,4 > take 5,6
    # 2,3 > take 3,4
    # Let's say we had 1,3. Could it ever be that 5,6 was closer?
    # No, because we already sorted on end times, so we know there is a start closer to 3 than 5,6.

    max_start_heap = []
    max_end_heap = []

    results = [-1 for _ in range(len(intervals))]

    for i in range(len(intervals)):
        heapq.heappush(max_start_heap, (-intervals[i][0], i))
        heapq.heappush(max_end_heap, (-intervals[i][1], i))

    for _ in range(len(intervals)):
        max_end, end_index = heapq.heappop(max_end_heap)

        if -max_start_heap[0][0] >= -max_end:
            # This can come after the end
            max_start, start_index = heapq.heappop(max_start_heap)

            # But we need to find the start that has the closest end...
            while max_start_heap and -max_start_heap[0][0] >= -max_end:
                max_start, start_index = heapq.heappop(max_start_heap)

            results[end_index] = start_index

            # This could be the start for the next end
            heapq.heappush(max_start_heap, (max_start, start_index))

    return results
