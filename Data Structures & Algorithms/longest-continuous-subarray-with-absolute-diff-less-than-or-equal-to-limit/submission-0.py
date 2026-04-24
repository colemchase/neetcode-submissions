import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        high = []
        low = []
        res = 0
        l = r = 0

        # loop nums with r
        while r < len(nums):
            # add rightmost num to window
            heapq.heappush(high, (-nums[r], r))
            heapq.heappush(low, (nums[r], r))

            # decrement leftmost while high and low is not valid
            while l <= r and high and -high[0][0] - low[0][0] > limit:
                l+=1
                while high and high[0][1] < l:
                    heapq.heappop(high)
                while low and low[0][1] < l:
                    heapq.heappop(low)
            # increment right
            # update res on r-l
            r+=1
            res = max(res, r-l)
        return res