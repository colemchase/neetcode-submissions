class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort() # lets us skip duplicates 

        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                continue
            
            l = i+1
            r = len(nums)-1
            while l < r:
                if l-1 != i and nums[l] == nums[l-1]:
                    l += 1
                    continue
                if r != len(nums)-1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                temp = nums[i] + nums[l] + nums[r]
                if temp == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif temp < 0:
                    l += 1
                else:
                    r -= 1
             
        return res