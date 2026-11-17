class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Naive
        # res = nums[0]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         prod = 1
        #         for num in nums[i:j]:
        #             prod *= num
        #         res = max(res, prod)
        # return res

        # Optimal Kadane's Algo

        # Move thru the nums
        # Should we add the num to the current total, or just restart??

        res = nums[0]
        curMin = 1
        curMax = 1

        for num in nums:
            temp = curMax * num
            curMax = max(temp, curMin*num, num)
            curMin = min(temp, curMin*num, num)
            res = max(res, curMax)

        return res

