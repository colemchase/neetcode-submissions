class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res = [-1, -1]

        if len(nums) == 0:
            return res

        def bs_low(l, h):
            if l == h:
                return l if nums[l] == target else -1
            
            mid = ((h-l) // 2) + l

            if nums[mid] >= target:
                return bs_low(l, mid)
            else:
                return bs_low(mid+1, h)

        def bs_high(l, h):
            if l == h:
                return l if nums[l] == target else -1
            
            mid = ((h-l) // 2) + l + 1

            if nums[mid] <= target:
                return bs_high(mid, h)
            else:
                return bs_high(l, mid-1)
        
        return [bs_low(0, len(nums)-1), bs_high(0, len(nums)-1)]

