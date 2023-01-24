import math

def fibonacci(n: int) -> int:
    """Write a function to calculate the nth Fibonacci number.

    Time: O(2^n)
    Space: O(n) for recursion stack.
    """
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_topdown(n: int) -> int:
    """Write a function to calculate the nth Fibonacci number.

    Time: O(n)
    Space: O(n)
    """
    dp = [-1 for _ in range(n+1)]
    return _fibonacci_topdown(n, dp)


def _fibonacci_topdown(n: int, dp: list[int]) -> int:
    """Recursive helper function."""
    if n <= 1:
        return n

    if dp[n] == -1:
        dp[n] = _fibonacci_topdown(n-1, dp) + _fibonacci_topdown(n-2, dp)

    return dp[n]


def fibonacci_bottomup(n: int) -> int:
    """Write a function to calculate the nth Fibonacci number.

    NOTE: We could optimize this to be O(1) space because we don't need
    the whole array, just the previous 2 numbers.

    Time: O(n)
    Space: O(n)
    """
    dp = [-1 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


def staircase(n: int) -> int:
    """
    Given a stair with ‘n’ steps, implement a method to count how
    many possible ways are there to reach the top of the staircase,
    given that, at every step you can either take 1 step, 2 steps,
    or 3 steps.

    Example:
        Stairs: 3 -> 4 (1, 1, 1), (1, 2), (2, 1), (3)

    Time: O(3^n)
    """
    if n == 0:
        return 1  # Reached the top, so 1 way to get there

    if n == 1:
        return 1  # Only 1 step to the end, so return 1

    if n == 2:
        return 2  # We can take two 1-steps or one 2-step

    num_ways = 0
    num_ways += staircase(n-1)
    num_ways += staircase(n-2)
    num_ways += staircase(n-3)

    return num_ways


def staircase_topdown(n: int) -> int:
    """
    Given a stair with ‘n’ steps, implement a method to count how
    many possible ways are there to reach the top of the staircase,
    given that, at every step you can either take 1 step, 2 steps,
    or 3 steps.

    Example:
        Stairs: 3 -> 4 (1, 1, 1), (1, 2), (2, 1), (3)

    Time: O(n)
    Space: O(n)
    """
    dp = [-1 for _ in range(n+1)]
    return _staircase_topdown(n, dp)


def _staircase_topdown(n: int, dp: list[int]) -> int:
    """Recursive helper function."""
    if n < 0:
        return 0

    if n == 0:
        return 1

    if n == 1:
        return 1

    if n == 2:
        return 2

    if dp[n] != -1:
        return dp[n]

    dp[n] = _staircase_topdown(n-1, dp) + _staircase_topdown(n-2, dp) + _staircase_topdown(n-3, dp)

    return dp[n]


def staircase_bottomup(n: int) -> int:
    """
    Given a stair with ‘n’ steps, implement a method to count how
    many possible ways are there to reach the top of the staircase,
    given that, at every step you can either take 1 step, 2 steps,
    or 3 steps.

    Example:
        Stairs: 3 -> 4 (1, 1, 1), (1, 2), (2, 1), (3)

    The intuition for this one is that if we look at the topdown pattern,
    we can see that we sum up the previous 3 values.

    Time: O(n)
    Space: O(n)
    [0, 1, 2, 3, 4]
     1  1  2  4
    """
    dp = [1, 1, 2]
    if n < 3:
        return dp[n]

    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])

    return dp[n]


def number_factors(n: int) -> int:
    """
    Given a number ‘n’, implement a method to count how many possible
    ways there are to express ‘n’ as the sum of 1, 3, or 4.

    n=4 -> 4 (1, 1, 1, 1), (1, 3), (3, 1), (4)

    Time: O(3^n)
    """
    if n < 0:
        return 0

    if n == 0:
        return 1

    if n == 1:
        return 1

    num_ways = 0
    num_ways += number_factors(n-1)
    num_ways += number_factors(n-3)
    num_ways += number_factors(n-4)

    return num_ways


def number_factors_topdown(n: int) -> int:
    """
    Given a number ‘n’, implement a method to count how many possible
    ways there are to express ‘n’ as the sum of 1, 3, or 4.

    n=4 -> 4 (1, 1, 1, 1), (1, 3), (3, 1), (4)
    """
    dp = [-1 for _ in range(n+1)]
    return _number_factors_topdown(n, dp)


def _number_factors_topdown(n: int, dp: list[int]) -> int:
    """Recursive helper function."""
    if n < 0:
        return 0

    if n <= 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = _number_factors_topdown(n-1, dp) + _number_factors_topdown(n-3, dp) + _number_factors_topdown(n-4, dp)

    return dp[n]


def number_factors_bottomup(n: int) -> int:
    """
    Given a number ‘n’, implement a method to count how many possible
    ways there are to express ‘n’ as the sum of 1, 3, or 4.

    n=4 -> 4 (1, 1, 1, 1), (1, 3), (3, 1), (4)
    """
    dp = [-1 for _ in range(n+1)]

    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 4

    for i in range(5, n+1):
        dp[i] = dp[i-1] + dp[i-3] + dp[i-4]

    return dp[n]


def minimum_jumps(jumps: list[int]) -> int:
    """
    Given an array of positive numbers, where each element represents the max number of
    jumps that can be made forward from that element, write a program to find the minimum
    number of jumps needed to reach the end of the array (starting from the first element).
    If an element is 0, then we cannot move through that element.

    Example:
        [2, 1, 1, 1, 4] -> 3 (0 > 2 > 3, 4)
    """
    # Solution:
    # For each index, try recursing with each possible number of jumps
    # Take the minimum
    # O(2^n)
    return _minimum_jumps(jumps, 0)


def _minimum_jumps(jumps: list[int], index: int) -> int:
    """Recursive helper functions."""
    if len(jumps) <= 0:
        return math.inf

    if index >= len(jumps):
        return math.inf

    if jumps[index] == 0:
        return math.inf  # Can't move from this position

    if index == len(jumps)-1:
        return 0

    min_jumps = math.inf

    possible_jumps = jumps[index]
    for i in range(1, possible_jumps+1):
        result = 1 + _minimum_jumps(jumps, index+i)
        if result != math.inf:
            min_jumps = min(min_jumps, result)

    return min_jumps


def minimum_jumps_topdown(jumps: list[int]) -> int:
    """
    Given an array of positive numbers, where each element represents the max number of
    jumps that can be made forward from that element, write a program to find the minimum
    number of jumps needed to reach the end of the array (starting from the first element).
    If an element is 0, then we cannot move through that element.

    Example:
        [2, 1, 1, 1, 4] -> 3 (0 > 2 > 3, 4)

                            jumps
     index
     0       1        2        3 ...
     1
     2
     3
     4
     5
    """
    # Solution:
    # Here we will memoize using a 2D array representing index and jumps
    max_jumps = max(jumps)
    dp = [-1 for _ in range(len(jumps))]
    return _minimum_jumps_topdown(jumps, 0, dp)


def _minimum_jumps_topdown(jumps: list[int], index: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if index >= len(jumps):
        return math.inf

    if jumps[index] == 0:
        return math.inf

    if index == len(jumps)-1:
        return 0

    if dp[index] != -1:
        return dp[index]

    possible_jumps = jumps[index]
    minimum_jumps = math.inf

    for i in range(1, possible_jumps+1):
        result = _minimum_jumps_topdown(jumps, index+i, dp)
        if result != math.inf:
            minimum_jumps = min(minimum_jumps, result+1)

    dp[index] = minimum_jumps

    return dp[index]


#def minimum_jumps_bottomup(jumps: list[int]) -> int:
    """
    Given an array of positive numbers, where each element represents the max number of
    jumps that can be made forward from that element, write a program to find the minimum
    number of jumps needed to reach the end of the array (starting from the first element).
    If an element is 0, then we cannot move through that element.

    Example:
        [2, 1, 1, 1, 4] -> 3 (0 > 2 > 3, 4)
    """
    # The intuition here is that while Fibonacci required us to look at the sum of
    #   the previous 2 numbers, this requires us to look a the min of the two numbers.
    # Think about it: Every index within range of the current index can be reached within
    # (jumps to current index) + 1
    # So for each index, we need to take min(current jump count, current index+1)
    # [inf, inf, inf, inf, inf]
    # [0, inf, inf, inf, inf]
    # [0, inf, inf, inf, inf], start=[0, 1, 2, 3]
    # [0, inf, inf, inf, inf], start=0, end=1
    # while 1 < 0 + 2... # Search within range
    # dp[1] = min(dp[1], dp[0]+1)
    # dp = [math.inf for _ in range(len(jumps))]
    # dp[0] = 0
    #
    # for start in range(len(jumps)):  # We know it just takes 1 jump to reach the last index
    #     #end = start + 1
    #     # while end <= start + jumps[start] and end < len(jumps):
    #     for end in range(start+1, start+jumps[start]+1):  # Check every cell in range (same as above)
    #         if end >= len(jumps):
    #             break  # Jumped off the end
    #         dp[end] = min(dp[end], dp[start]+1)
    #         end += 1
    #
    # return dp[len(jumps)-1]


def minimum_jumps_bottomup(jumps: list[int]) -> int:
    """
    Given an array of positive numbers, where each element represents the max number of
    jumps that can be made forward from that element, write a program to find the minimum
    number of jumps needed to reach the end of the array (starting from the first element).
    If an element is 0, then we cannot move through that element.

    Example:
        [2, 1, 1, 1, 4] -> 3 (0 > 2 > 3, 4)
    """
    dp = [math.inf for _ in range(len(jumps))]
    dp[0] = 0

    for start in range(len(jumps)):
        for end in range(start+1, start+jumps[start]+1):
            if end >= len(jumps):
                break

            dp[end] = min(dp[end], dp[start]+1)

    return dp[len(jumps)-1]


def minimum_jumps_with_fee(stairs: list[int]) -> int:
    """
    Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that
    you have to pay if you take the step. Implement a method to calculate the minimum fee
    required to reach the top of the staircase (beyond the top-most step). At every step,
    you have an option to take either 1 step, 2 steps, or 3 steps. You should assume that
    you are standing at the first step.

    Example:
        [1, 2, 5, 2, 1, 1] -> 3 (0 > 3 > end) Cost=1+2==3
    """
    return _minimum_jumps_with_fee(stairs, 0)


def _minimum_jumps_with_fee(stairs: list[int], index: int) -> int:
    """Recursive helper function."""

    # In this problem, the aim is to beyond the top of the staircase
    if index >= len(stairs):
        return 0

    # If we had to reach the top element, we could check if we overran and return
    # math.inf, for example, and then check the result before taking min.

    minimum_fee = math.inf

    for i in range(1, 4):
        result = _minimum_jumps_with_fee(stairs, index+i)
        minimum_fee = min(stairs[index] + result, minimum_fee)

    return minimum_fee


def minimum_jumps_with_fee_topdown(stairs: list[int]) -> int:
    """
    Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that
    you have to pay if you take the step. Implement a method to calculate the minimum fee
    required to reach the top of the staircase (beyond the top-most step). At every step,
    you have an option to take either 1 step, 2 steps, or 3 steps. You should assume that
    you are standing at the first step.

    Example:
        [1, 2, 5, 2, 1, 1] -> 3 (0 > 3 > end) Cost=1+2==3
    """
    dp = [-1 for _ in range(len(stairs))]
    return _minimum_jumps_with_fee_topdown(stairs, 0, dp)


def _minimum_jumps_with_fee_topdown(stairs: list[int], index: int, dp: list[int]) -> int:
    """Recursive helper function."""
    if index >= len(stairs):
        return 0

    if dp[index] != -1:
        return dp[index]

    minimum_jumps = math.inf

    for i in range(1, 4):
        result = _minimum_jumps_with_fee_topdown(stairs, index+i, dp)
        minimum_jumps = min(result+stairs[index], minimum_jumps)

    dp[index] = minimum_jumps

    return dp[index]


def minimum_jumps_with_fee_bottomup(stairs: list[int]) -> int:
    """
    Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that
    you have to pay if you take the step. Implement a method to calculate the minimum fee
    required to reach the top of the staircase (beyond the top-most step). At every step,
    you have an option to take either 1 step, 2 steps, or 3 steps. You should assume that
    you are standing at the first step.

    Example:
        [1, 2, 5, 2, 1, 1] -> 3 (0 > 3 > end) Cost=1+2==3
    """
    # dp=[0, 1, 1, 0, 0, 0], 1 and 2 can be reached for cost of first square
    # i=2, dp=[0, 1, 1, 0, 0, 0], cost to reach 3 is the min of:
    #       (cost to reach 2 + cost of 2, cost to reach 1 + cost of 1, cost to reach 0 + cost of 0)
    # i=2, dp=[0, 1, 1, 1, 0, 0, 0]
    # i=3, dp=[0, 1, 1, 1, 3, 0, 0]
    # i=4, dp=[0, 1, 1, 1, 3, 3, 0]
    # etc.
    # We take the minimum of the previous 3 costs/indices.
    dp = [0 for _ in range(len(stairs)+1)]

    dp[0] = 0  # No fee for 0 steps
    dp[1] = stairs[0]  # Only 1 step: we have to pay it's fee
    dp[2] = stairs[0]  # We HAVE to pay the fee for the first step, and we can reach
    # second step from there.

    for i in range(2, len(stairs)):
        dp[i+1] = min(stairs[i] + dp[i],
                      stairs[i-1] + dp[i-1],
                      stairs[i-2] + dp[i-2])

    return dp[len(stairs)]


def house_thief(houses: list[int]) -> int:
    """
    There are n houses built in a line. A thief wants to steal the maximum possible
    money from these houses. The only restriction the thief has is that he can’t
    steal from two consecutive houses, as that would alert the security system.
    How should the thief maximize his stealing?

    Example:
        [2, 5, 1, 3, 6, 2, 4] -> 15 (steal from houses worth 5, 6, 4)
    """
    # Solution: Try to recurse from this index, and next index and see which is worth more
    # It's the same as prev try with this, and then try without it.
    return _house_thief(houses, 0)


def _house_thief(houses: list[int], index: int) -> int:
    """Recursive helper function."""
    if index >= len(houses):
        return 0

    with_this_house = houses[index] + _house_thief(houses, index+2)
    without_this_house = _house_thief(houses, index+1)

    return max(with_this_house, without_this_house)


def house_thief_topdown(houses: list[int]) -> int:
    """
    There are n houses built in a line. A thief wants to steal the maximum possible
    money from these houses. The only restriction the thief has is that he can’t
    steal from two consecutive houses, as that would alert the security system.
    How should the thief maximize his stealing?

    Example:
        [2, 5, 1, 3, 6, 2, 4] -> 15 (steal from houses worth 5, 6, 4)
    """
    # Solution: Try to recurse from this index, and next index and see which is worth more
    # It's the same as prev try with this, and then try without it.
    # As we can see, we recurse from the same indices several times
    dp = [-1 for _ in range(len(houses))]
    return _house_thief_topdown(houses, 0, dp)


def _house_thief_topdown(houses: list[int], index: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if index >= len(houses):
        return 0

    if dp[index] != -1:
        return dp[index]

    with_this_house = houses[index] + _house_thief_topdown(houses, index+2, dp)
    without_this_house = _house_thief_topdown(houses, index+1, dp)

    dp[index] = max(with_this_house, without_this_house)

    return dp[index]


def house_thief_bottomup(houses: list[int]) -> int:
    """
    There are n houses built in a line. A thief wants to steal the maximum possible
    money from these houses. The only restriction the thief has is that he can’t
    steal from two consecutive houses, as that would alert the security system.
    How should the thief maximize his stealing?

    Example:
        [2, 5, 1, 3, 6, 2, 4] -> 15 (steal from houses worth 5, 6, 4)

    houses=[2, 5, 1, 3]
    dp=[0, 2, 0, 0, 0]
    > For each element, take max(previous house,
    """
    dp = [0 for _ in range(len(houses)+1)]
    dp[0] = 0  # 0 houses, so no value
    dp[1] = houses[0]  # If only 1 house, take that

    for i in range(2, len(houses)+1):
        # At each stage, we either take the previous-2 element + cost, or the previous element.
        dp[i] = max(dp[i-2] + houses[i-1], dp[i-1])

    return dp[len(houses)]
