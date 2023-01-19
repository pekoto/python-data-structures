import math


def unbounded_knapsack(profits: list[int], weights: list[int], capacity: int) -> int:
    """
    Given a list of profits, weights and capacity, find the maximum profit IF
    the number of items you can take are unbounded.

    Example:
    Items: {Apple, Orange, Melon}
    Weights: {1, 2, 3}
    Profits: {15, 20, 50}

    5 apples -> 75 profit
    1 apple + 2 orange -> 55 profit
    2 apples 1 melon -> 80 profit [Max profit]
    1 orange + 1 melon -> 70 profit
    """
    # Solution:
    # Recurse choosing the item, and then not choosing the item.
    # Terminating condition is when our index runs off the end of the array.
    # Capacity: 5, [1, 2, 3], [15, 20, 50], profit: 15
    #               ^
    # Capacity: 4, [1, 2, 3], [15, 20, 50], profit: 30
    #               ^
    # Capacity: 3, [1, 2, 3], [15, 20, 50], profit: 45
    #               ^
    # Capacity: 2, [1, 2, 3], [15, 20, 50], profit: 60
    #               ^
    # Capacity: 1, [1, 2, 3], [15, 20, 50], profit: 75
    #               ^
    # Capacity: 0, [1, 2, 3], [15, 20, 50], profit: 75
    #               ^
    # Now we hit 0 capacity, so we backtrack to 1 and try taking item 2 etc...
    # Time: O(2^n+c) -- n items + capacity
    # Space: O(n + c) -- to store recursion stack
    return _unbounded_knapsack(profits, weights, capacity, 0)


def _unbounded_knapsack(profits: list[int], weights: list[int], capacity: int, index: int) -> int:
    """Recursive helper function."""
    if index >= len(profits) or capacity <= 0:
        return 0

    # Try choosing this item.
    profit_with_item = 0

    if weights[index] <= capacity:
        profit_with_item = profits[index] + _unbounded_knapsack(profits, weights, capacity-weights[index], index)

    profit_without_item = _unbounded_knapsack(profits, weights, capacity, index+1)

    return max(profit_with_item, profit_without_item)


def unbounded_knapsack_topdown(profits: list[int], weights: list[int], capacity: int) -> int:
    """
    Given a list of profits, weights and capacity, find the maximum profit IF
    the number of items you can take are unbounded.

    Example:
    Items: {Apple, Orange, Melon}
    Weights: {1, 2, 3}
    Profits: {15, 20, 50}

    5 apples -> 75 profit
    1 apple + 2 orange -> 55 profit
    2 apples 1 melon -> 80 profit [Max profit]
    1 orange + 1 melon -> 70 profit
    """
    # Solution:
    # Recurse choosing the item, and then not choosing the item.
    # Terminating condition is when our index runs off the end of the array.
    # Capacity: 5, [1, 2, 3], [15, 20, 50], profit: 15
    #               ^
    # Capacity: 4, [1, 2, 3], [15, 20, 50], profit: 30
    #               ^
    # Capacity: 3, [1, 2, 3], [15, 20, 50], profit: 45
    #               ^
    # Capacity: 2, [1, 2, 3], [15, 20, 50], profit: 60
    #               ^
    # Capacity: 1, [1, 2, 3], [15, 20, 50], profit: 75
    #               ^
    # Capacity: 0, [1, 2, 3], [15, 20, 50], profit: 75
    #               ^
    # Now we hit 0 capacity, so we backtrack to 1 and try taking item 2 etc...
    # With this approach we memoize each result in a cache.
    # Time: O(n*c) -- size of our memoization array
    # Space: O(n*c)
    # Profits = rows, Capacity = columns
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
    return _unbounded_knapsack_topdown(profits, weights, capacity, 0, dp)


def _unbounded_knapsack_topdown(
        profits: list[int], weights: list[int], capacity: int, index: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if index >= len(profits) or capacity <= 0:
        return 0

    # Try choosing this item.
    profit_with_item = 0

    if dp[index][capacity] == -1:
        if weights[index] <= capacity:
            profit_with_item = profits[index] + _unbounded_knapsack_topdown(
                profits, weights, capacity-weights[index], index, dp)

        profit_without_item = _unbounded_knapsack_topdown(profits, weights, capacity, index+1, dp)

        dp[index][capacity] = max(profit_with_item, profit_without_item)

    return dp[index][capacity]


def unbounded_knapsack_bottomup(profits: list[int], weights: list[int], capacity: int) -> int:
    """
    Given a list of profits, weights and capacity, find the maximum profit IF
    the number of items you can take are unbounded.

    Example:
    Items: {Apple, Orange, Melon}
    Weights: {1, 2, 3}
    Profits: {15, 20, 50}

    5 apples -> 75 profit
    1 apple + 2 orange -> 55 profit
    2 apples 1 melon -> 80 profit [Max profit]
    1 orange + 1 melon -> 70 profit
    """
    # Solution:
    # In this case, we will build up a matrix with item as the row and capacity as the column.
    # In each case, we will either exclude the item (take weight from row above) or
    #   include the item -- take the weight of the item, plus profit from remaining capacity.
    #
    # Profit  | Weight | Index   | Capacity
    #                                0    1     2      3      4     5
    #   15        1       0          0    15    30     45    60     75
    #   50        3       1          0    15    30     50    65     80
    #   60        4       2          0    ...
    #   90        5       3          0
    #
    # Time: O(n*c) -- size of our memoization array
    # Space: O(n*c)
    # Profits = rows, Capacity = columns
    rows = len(profits)
    dp = [[-1 for _ in range(capacity+1)] for _ in range(rows)]

    # For 0 capacity, we can make 0 profit
    for row in range(rows):
        dp[row][0] = 0

    for index in range(rows):
        for cap in range(1, capacity+1):
            profit_with_this_item_only = 0
            profit_for_previous_item = 0

            if weights[index] <= cap:  # Row is the index of this item
                # Get the profit for this item + however many more of this item we could carry
                profit_with_this_item_only = profits[index] + dp[index][cap - weights[index]]
            if index > 0:
                # Check combinations taking previous items.
                profit_for_previous_item = dp[index-1][cap]

            dp[index][cap] = max(profit_with_this_item_only, profit_for_previous_item)

    return dp[rows-1][capacity]


def rod_cutting(lengths: list[int], prices: list[int], remaining_length: int) -> int:
    """
    Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that
    will maximize the profit. We are also given the price of every piece of length ‘i’ where
    ‘1 <= i <= n’.

    Example:
    Lengths: [1, 2, 3, 4, 5]
    Prices: [2, 6, 7, 10, 13]
    Rod Length: 5

    5xlength 1 = 10 profit
    2xlength 2 + 1xlength 1 = 14 profit
    1xlength 3 + 2xlength 2 = 11 profit
    etc.
    """
    return _rod_cutting(lengths, prices, remaining_length, 0)


def _rod_cutting(lengths: list[int], prices: list[int], remaining_length: int, index: int) -> int:
    """Recursive helper function."""
    if index >= len(lengths) or remaining_length <= 0:
        return 0

    profit_with_this_item = 0

    # Try taking this item
    if lengths[index] <= remaining_length:
        profit_with_this_item = prices[index] + _rod_cutting(lengths, prices, remaining_length-lengths[index], index)

    profit_without_this_item = _rod_cutting(lengths, prices, remaining_length, index+1)

    return max(profit_with_this_item, profit_without_this_item)


def rod_cutting_topdown(lengths: list[int], prices: list[int], remaining_length: int) -> int:
    """
    Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that
    will maximize the profit. We are also given the price of every piece of length ‘i’ where
    ‘1 <= i <= n’.

    Example:
    Lengths: [1, 2, 3, 4, 5]
    Prices: [2, 6, 7, 10, 13]
    Rod Length: 5

    5xlength 1 = 10 profit
    2xlength 2 + 1xlength 1 = 14 profit
    1xlength 3 + 2xlength 2 = 11 profit
    etc.
    """
    # Top-down memoization, takes O(n*remaining_length) time and space
    dp = [[-1 for _ in range(remaining_length+1)] for _ in range(len(lengths))]
    return _rod_cutting_topdown(lengths, prices, remaining_length, 0, dp)


def _rod_cutting_topdown(
        lengths: list[int], prices: list[int], remaining_length: int, index: int, dp: list[list[int]]) -> int:
    """Recursive helper function."""
    if index >= len(lengths) or remaining_length <= 0:
        return 0

    profit_with_this_item = 0

    # Try taking this item
    if dp[index][remaining_length] == -1:
        if lengths[index] <= remaining_length:
            profit_with_this_item = prices[index] + _rod_cutting_topdown(lengths, prices, remaining_length-lengths[index], index, dp)

        profit_without_this_item = _rod_cutting_topdown(lengths, prices, remaining_length, index+1, dp)

        dp[index][remaining_length] = max(profit_with_this_item, profit_without_this_item)

    return dp[index][remaining_length]


def rod_cutting_bottomup(lengths: list[int], prices: list[int], remaining_length: int) -> int:
    """
    Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that
    will maximize the profit. We are also given the price of every piece of length ‘i’ where
    ‘1 <= i <= n’.

    Example:
    Lengths: [1, 2, 3, 4, 5]
    Prices: [2, 6, 7, 10, 13]
    Rod Length: 5

    5xlength 1 = 10 profit
    2xlength 2 + 1xlength 1 = 14 profit
    1xlength 3 + 2xlength 2 = 11 profit
    etc.
    """
    # Bottom-up memoization, takes O(n*remaining_length) time and space
    rows = len(lengths)

    dp = [[-1 for _ in range(remaining_length+1)] for _ in range(rows)]

    for row in range(rows):
        dp[row][0] = 0  # For 0 length, we have 0 profit

    for item in range(rows):
        for length in range(1, remaining_length+1):
            price_with_this_item = 0
            price_without_this_item = 0
            if lengths[item] <= length:
                price_with_this_item = prices[item] + dp[item][length - lengths[item]]
            if item > 0:
                price_without_this_item = dp[item-1][length]

            dp[item][length] = max(price_with_this_item, price_without_this_item)

    return dp[rows-1][remaining_length]


def coin_change(denominations: list[int], amount: int) -> int:
    """
    Given an infinite supply of ‘n’ coin denominations and a total money amount,
    we are asked to find the total number of distinct ways to make up that amount.

    Example:
        Denominations: {1, 2, 3}, Amount: 5 -> 5
        {1, 1, 1, 1, 1}
        {1, 1, 1, 2}
        {1, 2, 2}
        {1, 1, 3}
        {2, 3}
    """
    # Try taking the current coin, and then without taking the current coin.
    return _coin_change(denominations, amount, 0)


def _coin_change(denominations: list[int], amount: int, index: int) -> int:
    """Recursive helper function."""
    if amount == 0:
        return 1

    if index >= len(denominations):
        return 0

    num_of_ways = 0

    if denominations[index] <= amount:
        num_of_ways += _coin_change(denominations, amount-denominations[index], index)

    num_of_ways += _coin_change(denominations, amount, index+1)

    return num_of_ways


def coin_change_topdown(denominations: list[int], amount: int) -> int:
    """
    Given an infinite supply of ‘n’ coin denominations and a total money amount,
    we are asked to find the total number of distinct ways to make up that amount.

    Example:
        Denominations: {1, 2, 3}, Amount: 5 -> 5
        {1, 1, 1, 1, 1}
        {1, 1, 1, 2}
        {1, 2, 2}
        {1, 1, 3}
        {2, 3}
    """
    # Try taking the current coin, and then without taking the current coin.
    dp = [[-1 for _ in range(amount+1)] for _ in range(len(denominations))]
    return _coin_change_topdown(denominations, amount, 0, dp)


def _coin_change_topdown(denominations: list[int], amount: int, index: int, dp: list[list[int]]) -> int:
    """Recursive helper functions."""
    if amount == 0:
        return 1

    if index >= len(denominations):
        return 0

    if dp[index][amount] == -1:
        num_of_ways = 0

        if denominations[index] <= amount:
            num_of_ways += _coin_change_topdown(denominations, amount-denominations[index], index, dp)

        num_of_ways += _coin_change_topdown(denominations, amount, index+1, dp)

        dp[index][amount] = num_of_ways

    return dp[index][amount]


def coin_change_bottomup(denominations: list[int], amount: int) -> int:
    """
    Given an infinite supply of ‘n’ coin denominations and a total money amount,
    we are asked to find the total number of distinct ways to make up that amount.

    Example:
        Denominations: {1, 2, 3}, Amount: 5 -> 5
        {1, 1, 1, 1, 1}
        {1, 1, 1, 2}
        {1, 2, 2}
        {1, 1, 3}
        {2, 3}
    """
    # Try taking the current coin, and then without taking the current coin.
    rows = len(denominations)
    dp = [[0 for _ in range(amount+1)] for _ in range(rows)]

    for row in range(rows):
        dp[row][0] = 1

    for item in range(rows):
        for amt in range(1, amount+1):
            num_of_ways = 0

            if denominations[item] <= amt:
                num_of_ways += dp[item][amt-denominations[item]]

            if item > 0:
                num_of_ways += dp[item-1][amt]

            dp[item][amt] = num_of_ways

    return dp[rows-1][amt]


def minimum_coin_change(denominations: list[int], amount: int) -> int:
    """
    Given an infinite supply of ‘n’ coin denominations and a total money amount,
    we are asked to find the minimum number of coins needed to make up that amount.

    Example:
        Denominations: {1, 2, 3}, Amount: 5 -> 2 (2, 3)
    """
    return _minimum_coin_change(denominations, amount, 0)


def _minimum_coin_change(denominations: list[int], amount: int, index: int) -> int:
    """Recursive helper function."""
    if amount == 0:
        return 0

    if index >= len(denominations):
        return math.inf

    num_with_this_coin = math.inf

    if denominations[index] <= amount:
        temp = _minimum_coin_change(denominations, amount-denominations[index], index)
        if temp != math.inf:  # Don't include if we overshot
            num_with_this_coin = temp + 1

    num_without_this_coin = _minimum_coin_change(denominations, amount, index+1)

    return min(num_with_this_coin, num_without_this_coin)


def minimum_coin_change_topdown(denominations: list[int], amount: int) -> int:
    """
    Given an infinite supply of ‘n’ coin denominations and a total money amount,
    we are asked to find the minimum number of coins needed to make up that amount.

    Example:
        Denominations: {1, 2, 3}, Amount: 5 -> 2 (2, 3)
    """
    dp = [[-1 for _ in range(amount+1)] for _ in range(len(denominations))]
    return _minimum_coin_change_topdown(denominations, amount, 0, dp)


def _minimum_coin_change_topdown(denominations: list[int], amount: int, index: int, dp: list[list[int]]) -> int:
    """Recursive helper functions."""
    if amount == 0:
        return 1

    if index >= len(denominations):
        return math.inf

    if dp[index][amount] == -1:
        num_with_this_coin = math.inf

        if denominations[index] <= amount:
            temp = _minimum_coin_change(denominations, amount - denominations[index], index)
            if temp != math.inf:  # Don't include if we overshot
                num_with_this_coin = temp + 1

        num_without_this_coin = _minimum_coin_change(denominations, amount, index + 1)

        dp[index][amount] = min(num_with_this_coin, num_without_this_coin)

    return dp[index][amount]


def minimum_coin_change_bottomup(denominations: list[int], amount: int) -> int:
    """
    Given an infinite supply of ‘n’ coin denominations and a total money amount,
    we are asked to find the minimum number of coins needed to make up that amount.

    Example:
        Denominations: {1, 2, 3}, Amount: 5 -> 2 (2, 3)
    """
    dp = [[math.inf for _ in range(amount+1)] for _ in range(len(denominations))]

    for i in range(len(denominations)):
        dp[i][0] = 0

    for index in range(len(denominations)):
        for amt in range(amount+1):
            amount_with_this_item = math.inf

            if index > 0:
                # Get the amount excluding this item.
                dp[index][amt] = dp[index-1][amt]
            if denominations[index] <= amt:
                if dp[index][amt-denominations[index]] != math.inf:
                    # Get the amount with this coin (+1)
                    dp[index][amt] = min(dp[index-1][amt], dp[index][amt-denominations[index]]+1)

    return -1 if dp[len(denominations)-1][amount] == math.inf else dp[len(denominations)-1][amount]


def maximum_ribbon_cut(lengths: list[int], n: int) -> int:
    """
    We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. We need to cut
    the ribbon into the maximum number of pieces that comply with the above-mentioned possible
    lengths. Write a method that will return the count of pieces.

    Example:
        lengths: [2, 3, 5], n=5 -> 2 [2, 3]
    """
    return _maximum_ribbon_cut(lengths, n, 0)


def _maximum_ribbon_cut(lengths: list[int], n: int, index: int) -> int:
    """Recursive helper function."""
    if n == 0:
        return 0

    if index >= len(lengths):
        return -math.inf

    cuts_with_length = -math.inf

    if lengths[index] <= n:
        result = _maximum_ribbon_cut(lengths, n-lengths[index], index)
        if result != math.inf:
            cuts_with_length = result + 1

    cuts_without_length = _maximum_ribbon_cut(lengths, n, index+1)

    return max(cuts_with_length, cuts_without_length)


def maximum_ribbon_cut_bottomup(lengths: list[int], n: int) -> int:
    """
    We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. We need to cut
    the ribbon into the maximum number of pieces that comply with the above-mentioned possible
    lengths. Write a method that will return the count of pieces.

    Example:
        lengths: [2, 3, 5], n=5 -> 2 [2, 3]
    """
    rows = len(lengths)
    dp = [[-1 for _ in range(n+1)] for _ in range(rows)]

    for row in range(rows):
        dp[row][0] = 0

    for index in range(rows):
        for length in range(1, n+1):
            cuts_with_length = -1
            cuts_without_length = -1

            if index > 0:
                cuts_without_length = dp[index-1][length]

            if lengths[index] <= length and dp[index][length-lengths[index]] != -1:
                cuts_with_length = dp[index][length-lengths[index]] + 1

            dp[index][length] = max(cuts_without_length, cuts_with_length)

    return dp[rows-1][length]
