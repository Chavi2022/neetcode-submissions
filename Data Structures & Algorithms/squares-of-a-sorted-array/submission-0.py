class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0,len(nums)-1
        res=[]
        while l<=r:
            x1=nums[l] ** 2 
            x2=nums[r] ** 2 
            if x1 > x2:
                res.append(x1)
                l+=1
            else:
                res.append(x2)
                r-=1
        return res[::-1]
            
            

                
