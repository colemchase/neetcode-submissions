class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        res = -1

        nums.sort()

        l = 0
        r = len(nums)-1
        while l < r:
            sm = nums[l] + nums[r]
            if sm < k:
                res = max(res, sm)
            if sm >= k:
                r-=1
            else:
                l+=1
            
        return res