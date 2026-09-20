class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        freqMap = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            c[i] = 1 + c.get(i,0)
        for num, i in c.items():
            freqMap[i].append(num)
        res = []
        for i in range(len(freqMap)-1,0,-1):
            for num in freqMap[i]:
                res.append(num)
                if len(res) == k:
                    return res


        
                
    
       