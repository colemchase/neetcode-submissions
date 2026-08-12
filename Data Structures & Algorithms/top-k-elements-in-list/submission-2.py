class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive count numbers, loop through keys to find highest num count, pop, repeat k-1 times
        cnt = Counter(nums)
        res = []
        maxq = [(-cnt[key], key) for key in cnt.keys()]
        heapq.heapify(maxq)
        while k > 0:
            k-=1
            res.append(heapq.heappop(maxq)[1])

        return res