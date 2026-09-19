class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pm = {0:1}
        curSum = 0
        res = 0
        for num in nums:
            curSum+=num
            diff = curSum - k
            res+= pm.get(diff,0)
            pm[curSum] = 1 + pm.get(curSum,0)
        return res


            
                


            


            

