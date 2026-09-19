class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """"
        sliding window approach

        """
        longest = 0
        l = 0
        for r in range(len(nums)):
            k -=(1 if nums[r] == 0 else 0)
            print("k : ",k)
            while k < 0:
                print("l ; ",l)
                k+=(1 if nums[l] == 0 else 0)
                l+=1
            
            longest = max(longest,r-l+1)
        return longest

            



