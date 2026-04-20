class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        linster = []
        for key in count:
            linster.append((count[key], key))
        linster = list(sorted(linster, key=lambda x: x[0], reverse=True))
        res = []
        for item in linster:
            res.append(item[1])
            if len(res) == k:
                return res
        return res