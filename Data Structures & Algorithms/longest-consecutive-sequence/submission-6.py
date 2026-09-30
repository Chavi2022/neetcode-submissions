class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #set(nums)
        #for num in nums
        # if num not in numSet, while num + length in nums: continue to iterate it
        numSet = set(nums)
        longest = 0
        for num in nums:
            curLen = 1
            if num -1 not in numSet:
                while (num + curLen) in numSet:
                    curLen+=1
                longest = max(longest,curLen)
        return longest
