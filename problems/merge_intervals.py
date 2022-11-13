from typing import List
import heapq


def merge_intervals_a(intervals: List[List[int]]) -> List[List[int]]:
    """
    Given a list of intervals, merge all the overlapping intervals to produce a list
    that has only mutually exclusive intervals.

    Intervals: [[1,4], [2,5], [7,9]] > Output: [[1,5], [7,9]]

    Time: O(n log n) for sorting
    Space: O(n) for return list + sorting
    """
    intervals.sort(key=lambda x: x[0])

    merged = []
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        if end < intervals[i][0]:
            merged.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]
        else:
            end = max(end, intervals[i][1])

    merged.append([start, end])

    return merged


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    Given a list of non-overlapping intervals sorted by their start time,
    insert a given interval at the correct position and merge all necessary
    intervals to produce a list that has only mutually exclusive intervals.

    Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
    Output: [[1,3], [4,7], [8,12]]
    """
    # If the new.start > end, don't merge -- must come after
    # If the new.end < start, don't merge it -- must come before
    # So, if new.start <= end and new.end >= start, merge it
    merged = []
    new_interval_merged = False

    # New interval should be added to start
    if new_interval[1] < intervals[0][0]:
        intervals.insert(new_interval, 0)
        new_interval_merged = True

    # New interval should be added to end
    if new_interval[0] > intervals[len(intervals)-1][1]:
        intervals.append(new_interval)
        new_interval_merged = True

    if not new_interval_merged:
        # First, let's merge the new interval
        for interval in intervals:
            if new_interval[0] <= interval[1] and new_interval[1] >= interval[0]:
                interval[0] = min(new_interval[0], interval[0])
                interval[1] = max(new_interval[1], interval[1])

    # Next, merge all of the intervals together
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        if end >= intervals[i][0]:
            end = max(end, intervals[i][1])
        else:
            merged.append([start, end])
            start = intervals[i][0]
            end = intervals[i][1]

    merged.append([start, end])

    return merged


def insert_interval_b(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """As above, just another approach."""
    merged = []
    i = 0  # Keep track of interval index.

    for interval in intervals:
        if interval[1] < new_interval[0]:
            merged.append(interval)
            i += 1  # Comes before -- end less than start
        else:
            break

    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        # If the start is > end, then new interval should come before
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1

    merged.append(new_interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged


def intervals_intersection(intervals_a: List[List[int]], intervals_b: List[List[int]]) -> List[List[int]]:
    """
    Given two lists of intervals, find the intersection of these two lists.
    Each list consists of disjoint intervals sorted on their start time.

    Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
    Output: [2, 3], [5, 6], [7, 7]

    # If end < start, comes before
    # If start > end, comes after
    # So if end >= start and start <= end, overlaps
    """
    intersections = []
    i = 0  # a pointer
    j = 0  # b pointer

    while i < len(intervals_a) and j < len(intervals_b):
        overlaps = False
        if intervals_a[i][0] <= intervals_b[j][1] and intervals_a[i][1] >= intervals_b[j][0]:
            overlaps = True

        if overlaps:
            intersections.append(
                [max(intervals_a[i][0], intervals_b[j][0]), min(intervals_a[i][1], intervals_b[j][1])])

        if intervals_a[i][1] < intervals_b[j][1]:
            i += 1
        else:
            j += 1

    return intersections


def conflicting_appointments(appointments: List[List[int]]) -> int:
    """
    Given an array of intervals representing ‘N’ appointments,
    find out if a person can attend all the appointments.

    Appointments: [[1,4], [2,5], [7,9]], Output: false
    Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
    """
    appointments.sort(key=lambda x: x[0])

    start = appointments[0][0]
    end = appointments[0][1]

    for i in range(1, len(appointments)):
        if end >= appointments[i][0]:
            return False

        start = appointments[i][0]
        end = appointments[i][1]

    return True


def min_meeting_rooms(meetings: List[List[int]]) -> int:
    """
    Given a list of intervals representing the start and end time of ‘N’ meetings,
    find the minimum number of rooms required to hold all the meetings.

    Meetings: [[1,4], [2,3], [3,6]] -> Output:2
    Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6],
    we need two rooms to hold all the meetings.

    Similar:
        Find max overlaps
        Given train arrival / departure times, find min platforms

    Solution: Use a min heap to keep track of end times, pop it while start >= end

    Time: O(n log n)
    Space: O(n)
    """
    if len(meetings) <= 1:
        return len(meetings)

    meetings.sort(key=lambda x: x[0])

    num_rooms = 0
    min_heap = []  # Keep track of the earliest finish time.
    start = 0
    end = 1

    for meeting in meetings:
        while len(min_heap) > 0 and meeting[start] >= min_heap[0][1][end]:
            heapq.heappop(min_heap)

        heapq.heappush(min_heap, (meeting[end], meeting))
        num_rooms = max(num_rooms, len(min_heap))

    return num_rooms


def max_cpu_load(processes: List[List[int]]) -> int:
    """
    We are given a list of Jobs. Each job has a Start time, an End time,
    and a CPU load when it is running. Our goal is to find the maximum CPU
    load at any time if all the jobs are running on the same machine.

    Jobs: [[1,4,3], [2,5,4], [7,9,6]] --> Output: 7
    Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7)
    will be when both the jobs are running at the same time i.e., during the time interval (2,4).
    """
    processes.sort(key=lambda x: x[0])

    start = 0
    end = 1
    load = 2
    current_load = 0
    min_heap = []

    max_load = 0

    for process in processes:
        while len(min_heap) > 0 and process[start] >= min_heap[0][1][end]:
            current_load -= heapq.heappop(min_heap)[1][load]

        current_load += process[load]
        heapq.heappush(min_heap, (process[end], process))
        max_load = max(max_load, current_load)

    return max_load
