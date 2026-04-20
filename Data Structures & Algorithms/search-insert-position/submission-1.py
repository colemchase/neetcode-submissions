class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def bs(l, h):
            if l >= h:
                if nums[l] < target:
                    return l + 1
                elif nums[l] >= target:
                    return l
                

            mid = (h+l) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return bs(mid+1, h)
            return bs(l, mid-1)

        return bs(0, len(nums)-1)
