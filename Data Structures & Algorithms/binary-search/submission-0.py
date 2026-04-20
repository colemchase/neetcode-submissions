class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bns(l, h):
            if l > h:
                return -1

            mid = (h+l) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                return bns(l, mid-1)

            return bns(mid+1, h)

        
        return bns(0, len(nums)-1)