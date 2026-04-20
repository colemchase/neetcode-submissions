class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = [i for i in range(100001)]
        for num in nums:
            if num > 0:
                arr[num] = 0
        for num in arr:
            if num != 0:
                return num