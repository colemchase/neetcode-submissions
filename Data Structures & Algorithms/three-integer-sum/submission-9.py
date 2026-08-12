class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Naive check each num to each num to each num (as long as not same index) to equal 
        
        nums.sort()
        res = []
        print(nums)

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums)-1
            while l < r:
                threesum = nums[l] + nums[r] + num 
                if threesum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r-=1
                
        return res