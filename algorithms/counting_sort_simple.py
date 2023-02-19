from collections import Counter


def counting_sort(nums: list[int]) -> list[int]:
    """A simple counting sort.

    In this counting sort, I use a frequency array where each index == the number,
    and the value at that index == the count of that numbers.

    Then I just iterate around it, appending the result.

    nums=[4, 4, 1, 2, 2, 3]
    counts={1:1, 2:2, 3:1, 4:2}
    freq=[0, 1, 2, 1, 2] (1 appears once, 2 appears twice, 3 appears once, 4 appears twice)
    result=[1, 2, 2, 3, 4, 4]

    Time: O(n+r) - where r is radix size, so good if r is close to n or fixed constant.
    Space: O(r)
    """
    counts = Counter(nums)
    frequency = [0 for _ in range(max(nums)+1)]

    for num, count in counts.items():
        frequency[num] = count  # The number at this index occurs count times.

    result = []

    for i in range(len(frequency)):
        number_of_times_i_repeats = frequency[i]
        for _ in range(number_of_times_i_repeats):
            result.append(i)

    return result
