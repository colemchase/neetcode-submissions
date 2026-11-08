class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # maximum subarry?? kadanes (n)
        cnt = defaultdict(int)
        maxGain = 0

        for num in nums:
            cnt[num] = max(cnt[num], cnt[k]) + 1
            maxGain = max(maxGain, cnt[num] - cnt[k])

        return cnt[k] + maxGain