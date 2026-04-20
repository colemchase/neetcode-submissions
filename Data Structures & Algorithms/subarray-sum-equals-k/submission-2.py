class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        hm = {0:1}
        currSum = 0

        for num in nums:
            currSum += num
            diff = currSum - k

            res += hm.get(diff, 0)
            hm[currSum] = hm.get(currSum, 0) + 1
        
        return res