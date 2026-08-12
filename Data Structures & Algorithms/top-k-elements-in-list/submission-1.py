class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive count numbers, loop through keys to find highest num count, pop, repeat k-1 times
        cnt = Counter(nums)
        res = []
        while k > 0:
            winner = None
            count = 0
            for key in cnt.keys():
                if cnt[key] > count:
                    count = cnt[key]
                    winner = key
            k-=1
            res.append(winner)
            del cnt[winner]

        return res