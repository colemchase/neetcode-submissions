class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights)-1
        res = 0

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r-l))  # update curr volume
            # should we move right or left  
            if heights[l] < heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            else:
                if heights[r-1] > heights[l+1]:
                    l+=1
                else:
                    r-=1
            
        return res