class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxP = 0
        for sell in prices:
            minPrice = min(minPrice,sell)
            maxP = max(maxP,sell-minPrice)
        return maxP