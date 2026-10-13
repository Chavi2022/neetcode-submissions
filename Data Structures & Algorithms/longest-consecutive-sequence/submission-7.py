class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        as long as num-1 in set we can increment longest


        """
        longest = 0
        numSet = set(nums)
        for i in nums:
            #if our num is in num set we can say as long as num -1 is it we can increment the curlen and set longest to be the max of itself and max
            if i-1 not in numSet:

                curLen = 0
                curr = i
                while curr in numSet:
                    curLen += 1
                    curr+=1
                longest = max(longest,curLen)
        return longest
