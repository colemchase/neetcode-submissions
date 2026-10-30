class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        
        nums.sort()


        # 3 4 5 6
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                return False

        return True
            
