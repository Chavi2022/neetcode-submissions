class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        -idea, 
        [1,2,4,6]-og
        [1,2,8,48]
        [48,48,24,6]
        
        [48,24,12,8]-res
        prefix_arr = [0]

for num in nums:
    # Append the last running total + the current number
    prefix_arr.append(prefix_arr[-1] + num)


    postfix_arr = [0] * (len(nums) + 1)

# Loop backwards from the last element to the first
for i in range(len(nums) - 1, -1, -1):
    postfix_arr[i] = nums[i] + postfix_arr[i + 1]

        """
        cur_run = 1
        pre = [1] * len(nums)
        for i in range(len(nums)):
            pre[i] = cur_run
            cur_run *= nums[i]
        runner = 1
        post = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            post[i] = runner
            runner *=nums[i]
        res = [post[i] * pre[i] for i in range(len(nums))]
        return res






