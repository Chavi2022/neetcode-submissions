class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num,freq in count.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        x = [i[1] for i in heap]
        return x[::-1]