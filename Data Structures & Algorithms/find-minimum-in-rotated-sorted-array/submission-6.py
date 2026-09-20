class Solution:
    def findMin(self, nums: List[int]) -> int:

        def bs(l, r):
            if r-l <= 1:
                return min(nums[r], nums[l])
            
            mid = ((r-l) // 2) + l
            print(nums[mid])
            if nums[l] < nums[mid]: # left sorted
                if nums[l] > nums[r]: # right
                    return bs(mid, r)
            return bs(l, mid)
        
        return bs(0, len(nums)-1)
            
