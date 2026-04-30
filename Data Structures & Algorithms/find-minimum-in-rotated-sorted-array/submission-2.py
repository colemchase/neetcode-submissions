class Solution:
    def findMin(self, nums: List[int]) -> int:

        def bs(l, h): 
            if h-l <= 1:
                return min(nums[l], nums[h])
            

            mid = l + (h-l) // 2
            
            # go to the left unless h is less than l
            if nums[h] < nums[l]:
                if nums[mid] < nums[h]:
                    return bs(l, mid)
                return bs(mid, h)
            
            return bs(l, mid)
        
        return bs(0, len(nums)-1)
