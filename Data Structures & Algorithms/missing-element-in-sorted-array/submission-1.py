import heapq

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        cnt = 0

        for i in range(1, len(nums)):
            for j in range(nums[i-1]+1, nums[i]):
                cnt += 1
                if cnt == k:
                    return j
        return k-cnt + nums[-1]