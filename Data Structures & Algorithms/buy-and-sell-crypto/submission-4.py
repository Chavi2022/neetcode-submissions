class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx,curr=0,prices[0]
        for sell in prices:
            maxx = max(sell-curr,maxx)
            curr = min(sell,curr)
        return maxx
            