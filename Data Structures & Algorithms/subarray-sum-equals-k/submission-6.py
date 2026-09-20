class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = {0:1}
        curSum,maxSum=0,0
        for num in nums:
            curSum+=num
            diff = curSum-k
            maxSum+=prefixMap.get(diff,0)
            prefixMap[curSum] = prefixMap.get(curSum,0)+1
        return maxSum


        

            
                


            


            

