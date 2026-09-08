class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        cur = 0
        for n in nums:
            if n == 1:
                cur+=1
                longest=max(longest,cur)
            else:
                cur=0
            
        return longest