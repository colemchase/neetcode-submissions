class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(l, r):
            if l >= r:
                return l if nums[l] == target else -1
            
            mid = (r+l) // 2
            if target == nums[mid]:
                return mid
    
            # find which side to go to
            # is target greater than left, but
            if target >= nums[l]:
                if target > nums[mid]:
                    if target > nums[r]:
                        if nums[mid] > nums[l]: 
                            return bs(mid+1, r) # 5
                        return bs(l, mid-1) # 3
                    return bs(mid+1, r) # 2
                # > < 
                if target > nums[r]:
                    return bs(l, mid-1) # 4 DUP 6
                return bs(l, mid-1) # 1

            if nums[mid] < nums[r] and target < nums[mid]:
                return bs(l, mid-1) # 9
            return bs(mid+1, r) # 7 & 8
        
        return bs(0, len(nums)-1)