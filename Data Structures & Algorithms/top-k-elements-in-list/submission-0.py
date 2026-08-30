class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        # q =deque()
        # for i in nums:
        #     if i in freq:
        #         freq[i]+=1
        #     freq[i]=1
            
        return list(item[0] for item in freq.most_common(k))

        
            