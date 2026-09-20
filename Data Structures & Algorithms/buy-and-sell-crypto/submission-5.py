class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        minp = prices[0]
        for sell in prices:
            mp = max(mp,sell-minp)
            minp = min(minp,sell)
        return mp