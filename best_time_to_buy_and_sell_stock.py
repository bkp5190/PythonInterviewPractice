from typing import List


def maxProfit(prices: List[int]) -> int:
    # Left is buy, Right is sell
    l, r = 0, 1

    # Initial max_profit to be 0 to start
    max_profit = 0

    # Iterate until the Right pointer reaches the end of the array
    while r < len(prices):
        # Profitable if the Right > Left
        if prices[r] > prices[l]:
            # Calculate the potential profit by subtracting
            profit = prices[r] - prices[l]
            # Update the max profit
            max_profit = max(max_profit, profit)
        # If this is a lower price than current, bring the Left pointer up
        else:
            l = r
        # Always increment the Right pointer as we iterate through the array
        r += 1

    # Return the final max_profit found
    return max_profit



assert maxProfit([7,1,5,3,6,4]) == 5

assert maxProfit([7,6,4,3,1]) == 0
