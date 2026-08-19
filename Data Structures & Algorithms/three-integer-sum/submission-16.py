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

        res = []
        nums.sort()
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                if l != i+1 and nums[l] == nums[l-1]:
                    l+=1
                    continue
                if r != len(nums)-1 and nums[r] == nums[r+1]:
                    r-=1
                    continue

                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                elif curr < 0:
                    l+=1
                else:
                    r-=1

        return list(res)
        