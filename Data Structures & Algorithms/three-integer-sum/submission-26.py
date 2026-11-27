class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                continue
            
            if i and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = len(nums)-1
            while j < k:
                if j > i+1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                
                if j < k:
                    curr = nums[i] + nums[j] + nums[k]
                    if curr == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        j+=1
                        k = len(nums)-1
                    elif curr < 0:
                        j += 1
                    else:
                        k -= 1

                
        return res

