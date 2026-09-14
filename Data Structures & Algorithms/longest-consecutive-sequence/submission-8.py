class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Naive:
        # sort n log n
        # if prev == curr-1    incr counter else reset
        # nums = list(set(nums))
        # nums.sort()
        # res = 1
        # count = 1
        # for i in range(1, len(nums)):
        #     if nums[i]-1 == nums[i-1]:
        #         count +=1
        #     else:
        #         count = 1
        #     res = max(count, res)

        # return res


        # Optimal o n
        # hm    num, consecutive nums above
        # only calculate if num-1 not in nums.  (only check heads)
        res = 0
        seth = set(nums)
        for num in nums:
            if num-1 not in seth: # beginning
                curr = num
                count = 0
                while curr in seth:
                    count+=1
                    curr += 1
                res = max(res, count)
                
        return res
