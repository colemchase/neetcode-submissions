class Solution:
    def countElements(self, arr: List[int]) -> int:
        hm  = {}
        for num in arr:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1
        res = 0
        for k in hm.keys():
            if k+1 in hm:
                res+=hm[k]
        return res
