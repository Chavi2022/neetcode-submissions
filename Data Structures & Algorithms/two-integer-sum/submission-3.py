class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        {}=, store every indecies/value, and we can check as we iterate, for i in range(len(nums)), check if target -nums[i] in {} return [seen[target-nums[i]],i] 

        """
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            tval = target-num
            if tval in seen:
                return [seen[tval],i]
            seen[num] = i
        return []