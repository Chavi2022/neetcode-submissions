class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        marea = 0
        while l<r:
            m = r-l
            lenn = min(heights[l],heights[r])
            marea = max(marea,lenn * m)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return marea
            