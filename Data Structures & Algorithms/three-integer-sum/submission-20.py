class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add((nums[i], nums[j], nums[k]))
        # return list(res)

        nums.sort() # helps skippings dups when moving thru nums
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > 0:
                break
            if i and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = n-1

            while j < k:
                if j-i > 1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                if k != n-1 and nums[k] == nums[k+1]:
                    k-=1
                    continue
                
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                elif curr < 0:
                    j+=1
                else:
                    k-=1
            
        return res
