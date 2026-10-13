class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [(2*4*6),(1*4*6),(1*2*6),(1*2*4)]->[48,24,12,8]
        okay, intuitively i see that we can utilize a prefix map

        """
        pre = [1] * len(nums)
        runner = 1
        for i in range(len(nums)):
            pre[i] = runner
            runner *= nums[i]

        post = [1] * len(nums)
        run = 1
        for i in range(len(nums)-1,-1,-1):
            post[i] = run
            run *= nums[i]
        return [post[i] * pre[i] for i in range(len(nums))]
