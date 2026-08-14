class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dict for tacking
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            tval = target - num
            #if the tval is in seen return the indecies if otherwise append to dict
            if tval in seen:
                return [seen[tval], i]
            seen[num] = i
        return []