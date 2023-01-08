import heapq
import sys


def merge_k_sorted_lists(sorted_lists: list[list[int]]) -> list[int]:
    """
    Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

    [2, 6, 8], [3, 6, 7], [1, 3, 4] -> [1, 2, 3, 3, 4, 6, 6, 7, 8]
    [5, 8, 9], [1, 7] -> [1, 5, 7, 8, 9]

    Note: I just used arrays here, but linked lists are essentially the same.

    Time: O(k*n log k), where k is number of lists
    Space: O(k), where k is number of lists, and n is max size of list
    """
    min_heap = []
    result = []

    for sorted_list in sorted_lists:
        # Element, list, index
        heapq.heappush(min_heap, (sorted_list[0], sorted_list, 0))

    while min_heap:
        elem, sorted_list, index = heapq.heappop(min_heap)
        result.append(elem)
        index += 1

        if index < len(sorted_list):
            heapq.heappush(min_heap, (sorted_list[index], sorted_list, index))

    return result


def kth_smallest_number(sorted_lists: list[list[int]], k: int) -> int:
    """
    Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

    [2, 6, 8], [3, 6, 7], [1, 3, 4] -> 4
    (1, 2, 3, 3, 4, 6, 6, 7, 8)

    - Given ‘M’ sorted arrays, find the median number among all arrays.
    """
    # 4, 6
    # so_far: 3
    # num: 3
    min_heap = []
    nums_so_far = 0

    for sorted_list in sorted_lists:
        heapq.heappush(min_heap, (sorted_list[0], sorted_list, 0))

    while min_heap:
        num, sorted_list, index = heapq.heappop(min_heap)
        index += 1
        nums_so_far += 1

        if nums_so_far == k:
            return num

        if index < len(sorted_list):
            heapq.heappush(min_heap, (sorted_list[index], sorted_list, index))

    return 0


def kth_smallest_number_in_matrix(matrix: list[list[int]], k: int) -> int:
    """
    Given an N*N matrix where each row and column is sorted in ascending order,
    find the Kth smallest element in the matrix.

    matrix = [
        [2, 6, 8],
        [3, 7, 10],
        [5, 8, 11]
    ], k=5 -> 7
    """
    # This is essentially the same problem: We just use rows in the matrix instead
    # NOTE: This can be done in a more optimal manner by using a binary search.
    min_heap = []
    nums_so_far = 0
    num = 0

    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        heapq.heappush(min_heap, (matrix[row][0], row, 0))

    while min_heap:
        num, row, index = heapq.heappop(min_heap)
        nums_so_far += 1
        index += 1

        if nums_so_far == k:
            break

        if index < len(matrix[row]):
            heapq.heappush(min_heap, (matrix[row][index], row, index))

    return num


def smallest_number_range(sorted_lists: list[list[int]]) -> list[int]:
    """
    Given ‘M’ sorted arrays, find the smallest range that includes at least one number
    from each of the ‘M’ lists.

    [1, 5, 8], [4, 12], [7, 8, 10] -> [4, 7] (contains 5, 4, and 7)
    [1, 9], [4, 12], [7, 10, 16] -> [9, 12] (contains 9, 12, and 10)
    """
    min_num = sys.maxsize
    max_num = -sys.maxsize-1

    min_heap = []

    for sorted_list in sorted_lists:
        max_num = max(max_num, sorted_list[0])
        min_num = min(min_num, sorted_list[0])

        heapq.heappush(min_heap, (sorted_list[0], sorted_list, 0))

    min_diff = max_num-min_num
    min_range = [min_num, max_num]

    while min_heap:
        num, sorted_list, index = heapq.heappop(min_heap)
        index += 1

        if index < len(sorted_list):
            next_num = sorted_list[index]

            heapq.heappush(min_heap, (next_num, sorted_list, index))

            max_num = max(max_num, next_num)
            diff = max_num - min_heap[0][0]

            if diff < min_diff:
                min_diff = diff
                min_range = [min_heap[0][0], max_num]
        else:
            break

    return min_range


def k_pairs_largest_sums(nums1: list[int], nums2: list[int], k: int) -> list[int]:
    """
    Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum
    where each pair consists of numbers from both the arrays.

    [9, 8, 2], [6, 3, 1], k=3 -> [9, 3], [9, 6], [8, 6]
    [5, 2, 1], [2, -1], k=3 -> [5, 2], [5, -1], [2, 2]
    """
    # [9, 8, 2]     [6, 3, 1]
    #     ^
    #                ^
    min_heap = []

    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):

            if len(min_heap) < k:
                heapq.heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:
                # Since lists are sorted in descending order, we won't be able to
                # get a bigger pair
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (nums1[i] + nums2[j], i, j))

    results = []

    for num, i, j in min_heap:
        results.append([nums1[i], nums2[j]])

    return results
