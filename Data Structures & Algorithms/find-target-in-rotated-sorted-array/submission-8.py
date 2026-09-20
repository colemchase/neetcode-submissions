class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(l, r):
            if r - l <= 1:
                if nums[r] == target:
                    return r
                return l if nums[l] == target else -1

            mid = ((r-l) // 2) + l

            if nums[mid] == target:
                return mid
            
            if nums[l] < nums[mid]: # left sorted
                if nums[l] <= target < nums[mid]:
                    return bs(l, mid-1)
                return bs(mid+1, r)
            
            # right sorted
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    return bs(mid+1, r)
            return bs(l, mid-1)

        return bs(0, len(nums) - 1)