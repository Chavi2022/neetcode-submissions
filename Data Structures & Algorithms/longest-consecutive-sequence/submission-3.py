class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestsequence = 0
        #for O(1)look up as inuitively we need to continuously check if num -1  doesnt exist
        numSet=set(nums)
        for num in nums:
            if (num-1) not in numSet:
                #init length so we can keep longestsequence as the max length
                length = 1
                #sliding window
                while (num + length) in numSet:
                    length+=1
                longestsequence = max(longestsequence,length)
        return longestsequence


            
