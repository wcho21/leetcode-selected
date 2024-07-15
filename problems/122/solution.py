# Accepted: 51ms (89.65%), 17.80MB (30.09%)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            curPrice = prices[i]
            nextPrice = prices[i+1]
            if curPrice > nextPrice:
                continue

            profit += nextPrice - curPrice

        return profit
