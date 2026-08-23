class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(l, r):
            if l == r: # base case
                return l if nums[l] == target else -1
            
            mid = ((r-l) // 2) + l # integer overflow safe

            if nums[mid] == target: # check mid
                return mid

            if nums[l] <= nums[mid]: # left side sorted
                if nums[l] <= target <= nums[mid]: # target should be in left side
                    return bs(l, mid-1)
                return bs(mid+1, r) # 

            if nums[mid] <= target <= nums[r]: # right side sorted
                return bs(mid+1, r) # target should in in right side

            return bs(l, mid-1) # target should be in unsorted left side
        
        return bs(0, len(nums)-1)