class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        arr[int], consec is n +1

        """
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num -1 not in numSet:
                cl = 1
                while (num+cl) in numSet:
                    cl+=1
                longest = max(longest,cl)
        return longest

            
            

