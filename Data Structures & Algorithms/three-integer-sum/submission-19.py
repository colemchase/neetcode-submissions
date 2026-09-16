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

        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            j = i+1
            k = n-1

            if i and nums[i] == nums[i-1]: # skip dup i
                continue
            if nums[i] > 0: # no chance of being total equal zero
                continue
            
            total = nums[i] + nums[j] + nums[k]
            while j < k:
                if total <= 0:
                    if not total:
                        res.append([nums[i], nums[j], nums[k]]) # valid solution
                    j+=1
                    while j < k and nums[j] == nums[j-1]: # skip dup j
                        j+=1

                if total > 0:
                    k-=1
                    while k > j and nums[k] == nums[k+1]: # skip dup k
                        k-=1    

                total = nums[i] + nums[j] + nums[k]

        return res
        