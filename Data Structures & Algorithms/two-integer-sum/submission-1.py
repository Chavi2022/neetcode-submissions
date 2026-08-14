class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            n = target - num
            if n in seen:
                return [seen[n],i]
            seen[num] = i
        return []