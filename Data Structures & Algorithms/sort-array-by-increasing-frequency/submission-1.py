class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        
        res = []
        arr = []
        for key in cnt.keys():
            arr.append((key, cnt[key]))
        arr.sort(key=lambda x: (x[1], -x[0]))
        for x in arr:
            res += [x[0]] * x[1]
        return res