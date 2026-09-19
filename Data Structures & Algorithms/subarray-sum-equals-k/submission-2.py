class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        res = 0
        hm = {0:1}
        for num in nums:
            curr+=num
            diff = curr - k
            res += hm.get(diff,0)
            hm[curr] = 1 + hm.get(curr,0)
        return res


            
                


            


            

