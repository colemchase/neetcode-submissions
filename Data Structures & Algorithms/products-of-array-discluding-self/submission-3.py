class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Naive:
        # loop through nums, set nums[i] equal to prod left * prod right
        # 1 2 3 4 5
        #     40
        # res = nums.copy()
        # for i in range(len(nums)):
        #     prod = 1
        #     for num in nums[:i]:
        #         prod *= num
        #     for num in nums[i+1:]:
        #         prod *= num
        #     res[i] = prod
        # return res

        # Optimal 
        # loop through nums, calculate prefix product of array (prod) for left and right
        left = [1] * len(nums) # prefix product
        for i, num in enumerate(nums[:-1]):
            left[i+1] = left[i] * nums[i]
        right = [1] * len(nums)
        for i in range(len(nums)-1, 0, -1):
            right[i-1] = right[i] * nums[i]

        # loop through nums again, set nums[i] = left prefix * right prefix
        for i in range(len(nums)):
            nums[i] = left[i] * right[i]
        return nums

