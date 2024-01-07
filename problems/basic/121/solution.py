# Accepted: 792ms (82.86%), 28.32MB (6.24%)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfitVal = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfitVal = max(maxProfitVal, price - minPrice)

        return maxProfitVal
