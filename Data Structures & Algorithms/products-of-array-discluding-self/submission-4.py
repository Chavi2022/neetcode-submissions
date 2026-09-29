class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        -idea, 
        [1,2,4,6]-og
        [1, 1, 2, 8]
        [48, 24, 6, 1]
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
        
        r = 1
        pre = [1] * len(nums)
        for i in range(len(nums)):
            pre[i] = r
            r *= nums[i]
        post = [1] * len(nums)
        rl = 1
        for i in range(len(nums)-1,-1,-1):
            post[i] = rl
            rl *= nums[i]
        return [post[i] * pre[i] for i in range(len(nums))]





