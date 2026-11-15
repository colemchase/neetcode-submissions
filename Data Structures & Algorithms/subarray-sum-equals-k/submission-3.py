class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        
        # prefix sum approach

        prefix = {0: 1} # previous sums of other previous subarrays

        curSum = 0
        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefix.get(diff, 0)
            prefix[curSum] = prefix.get(curSum, 0) + 1

        return res