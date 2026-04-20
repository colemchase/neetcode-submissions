class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()

        for i in range(len(nums)):
            target = 0 - nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] < target:
                    j+=1
                elif nums[j] + nums[k] > target:
                    k-=1
                else:

                    curr = (nums[i], nums[j], nums[k])
                    res.add(curr)     
                    j+=1
                    k-=1

        return [[item[0], item[1], item[2]] for item in res]