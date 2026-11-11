class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        leftMax = 0
        rightMax = 0
        
        res = 0
        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            res += leftMax - height[l]
            res += rightMax - height[r]
            if leftMax < rightMax:
                l+=1
            else:
                r-=1
        
        return res