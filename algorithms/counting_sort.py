from typing import List


def counting_sort(items: List[int]) -> None:
    """A counting sort implementation.

    A counting sort is good for sorting something with a small radix,
    for example, enums.

    * Set up array to hold counts (max val + 1)
    * Get the cumulative counts of each item in that array
    * Iterate around the input array:
        - The sorted pos = counts[input_elem]-1
        - Decrement count by 1
    " Finally, copy the output array back to the main array

    Time: O(n+r), n = array size, r = radix size
                    n = loop over array
                    r = get counts
    Space: O(n+r)

    Stable: Yes
    """
    # Sets up an array to hold the counts of each element.
    max_val = max(items)+1
    counts = [0] * max_val

    # Sets up an auxiliary array to hold the output.
    output = [0] * len(items)

    # Stores the count of each element.
    # [4, 4, 2, 1] -> [0, 1, 1, 0, 2]
    for item in items:
        counts[item] += 1

    # Stores the cumulative counts of each element.
    # [0, 1, 1, 0, 2] -> [0, 1, 2, 2, 4]
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    # Copy to output. The correct pos is given by count array val -1.
    # items = [4, 4, 2, 1]
    # counts = [0, 1, 1, 2, 3]
    # output = [.., .., .., 4] <- count[4-1] = count[3]
    for item in items:
        output_index = counts[item]-1
        output[output_index] = item
        counts[item] -= 1

    # Copy back to the original list
    for i, elem in enumerate(output):
        items[i] = elem
