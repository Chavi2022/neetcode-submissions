class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        return [item for item, count in x.most_common(k)]