class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        v = c.most_common(k)
        return [item[0] for item in v]

