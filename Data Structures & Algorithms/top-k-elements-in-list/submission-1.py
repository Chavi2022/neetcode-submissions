class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        q =deque()
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        v = sorted(freq.keys(),key=lambda x:freq[x],reverse=True)
        for i in range(k):
            q.append(v[i])  
        return list(q)  

        
            