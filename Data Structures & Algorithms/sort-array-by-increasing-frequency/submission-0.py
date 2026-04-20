class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        
        sorting = []
        for key in cnt.keys():
            sorting.append((key, cnt[key]))

        sorting.sort(key=lambda x: (x[1], -x[0]))
        res = []
        for i in range(len(sorting)):
            curr = sorting[i]
            res += [curr[0]] * curr[1]
        
        return res