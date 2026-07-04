class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums)
        # apply the operation to the min and push it, do this k times
        for _ in range(k):
            num, i = heapq.heappop(nums)
            heapq.heappush(nums, (num*multiplier, i))
        # turn back into list and return
        res = nums[:]
        for num, i in nums:
            res[i] = num

        return res