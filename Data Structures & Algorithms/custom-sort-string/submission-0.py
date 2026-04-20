class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)

        
        res = []
        for c in order:
            res += [c] * cnt[c]
        order = set(order)
        for key in cnt.keys():
            if key not in order:
                res += [key] * cnt[key]

        return "".join(res)