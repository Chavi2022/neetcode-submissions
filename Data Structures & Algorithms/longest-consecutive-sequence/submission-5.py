class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        arr[int], consec is n +1
        set(nums),
        if num -1 is in our numset:

        -> if num-1 not in numSet:
            lenn = 1
            while num + lenn:
                lenn+=1
            maxx = max(lenn,max)

        """
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if (num-1) not in numSet:
                l = 1
                while (num+l) in numSet:
                    l+=1
                longest = max(longest,l)
        return longest
        

            
            

