class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                threesum = nums[i] + nums[j] + nums[k]
                if threesum < 0:
                    j+=1
                elif threesum > 0:
                    k-=1
                else:
                    curr = [nums[i], nums[j], nums[k]]
                    res.append(curr)
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
            if nums[i] == 0:
                break

        return res