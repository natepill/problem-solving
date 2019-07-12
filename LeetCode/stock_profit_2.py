"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

"""

# When we sell stock we cooldown and that can be considered an index + 2

def maxProfit(prices):
    # Input: [1,2,3,0,2]

    # init buy and sell at first val
    # init curr_profit

    # iterate over list
        # if val is less than the next val
            # then buy that stock
        # if greater than next value
            # if bought stock
            #     sell stock, add to profit
            # otherwise continue

    bought = (False, 0)
    curr_profit = 0

    for index,price in enumerate(prices):
        if price < prices[index+1] and not bought[0]:
            curr_profit += 

if __name__ == "__main__":

    # Input: [7,1,5,3,6,4]
    # Output: 7
    input = [7,1,5,3,6,4]
    print(maxProfit(input))
