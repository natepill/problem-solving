
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""

def maxProfit(prices):

    potential_profit = 0
    highest = prices[0]
    lowest = prices[0]

    for price in prices:
        if price > highest:
            highest = price

        if price < lowest:
            lowest = price
            highest = price
            continue

        if highest-lowest > potential_profit:
            potential_profit = highest-lowest

    return potential_profit
    # return max(potential_profits)

if __name__ == "__main__":

    # Input: [7,1,5,3,6,4]
    # Output: 5

    input = [7,1,5,3,6,4]
    print(maxProfit(input))
