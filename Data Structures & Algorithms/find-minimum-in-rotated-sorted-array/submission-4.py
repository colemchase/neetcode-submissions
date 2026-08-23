class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def bs(l, r):
            if r-l <= 2:
                return min(nums[l:r+1])
            
            if l < r: # still searching
                mid = ((r-l) // 2) + l # safe diff
                
                if nums[l] <= nums[mid]:# left sorted
                    if nums[l] < nums[r]: # left has smaller
                        return bs(l, mid)
                    return bs(mid, r) # right has smaller
                return bs(l, mid)

        return bs(0, len(nums)-1)