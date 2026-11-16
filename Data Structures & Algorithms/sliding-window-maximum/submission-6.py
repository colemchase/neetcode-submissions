class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        mono = []
        for i in range(k-1):
            while mono and nums[i] > nums[mono[-1]]:
                mono.pop()
            mono.append(i)

        for i in range(k-1, len(nums)):
            while mono and nums[i] > nums[mono[-1]]:
                mono.pop()
            while mono and i-mono[0] >= k:
                mono.pop(0)
            mono.append(i)
            res.append(nums[mono[0]])

        return res
        