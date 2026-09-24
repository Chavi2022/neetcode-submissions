class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        x = Counter(nums)
        heap =[]
        for num,freq in x.items():
            #push onto heap
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        res = []
        for _, num in heap:
            res.append(num)
        return res


        
                
    
       