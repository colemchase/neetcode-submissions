class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0

        for i in range(len(nums)):
            curr = nums[i]
            if curr % 2 == 0:
                temp = nums[l]
                nums[l] = curr
                nums[i] = temp
                l+=1

        return nums