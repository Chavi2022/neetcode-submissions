class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        x = [item[0] for item in freq.most_common(k)]
        return x

        
            