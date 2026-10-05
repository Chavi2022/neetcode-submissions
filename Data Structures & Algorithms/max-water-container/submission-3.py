class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        min(l,r) * r-l
        
        """
        l,r = 0,len(heights)-1
        maxWater = 0
        while l < r:
            cWater = 0
            if heights[l] < heights[r]:
                cWater = heights[l] * (r-l)
                l+=1

                # print("(r-l)",(r-l), r,l,heights[l])
                # print("cWater",cWater)
            else:
                cWater = heights[r] * (r-l)
                r-=1
                # print("(r-l)2",(r-l),r,l,heights[r])
                # print("cWater2",cWater)
            maxWater = max(cWater,maxWater)
        return (maxWater)
