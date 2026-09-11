class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #product of post and prefix must be stored in a res, res[1] * n as if there is nothing adjacent it must be self
        n = len(nums)
        res =[1] *n
        #this being [1,1,1,1]
        #want to use post and prefix
        pre = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(n-1,-1,-1):
            res[i] *= post
            post *= nums[i]
        return res
