class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Brutal
        # double for each different contianer possible
        # res = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         h = min(heights[i], heights[j])
        #         w = j-i
        #         res = max(res, h * w)

        # return res

        # Optimal
        # Two pointer 
        res = 0
        l = 0
        r = len(heights)-1

        while l < r:
            res = max(res, min(heights[l], heights[r])*(r-l) )
            # do we increment l or r
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return res

