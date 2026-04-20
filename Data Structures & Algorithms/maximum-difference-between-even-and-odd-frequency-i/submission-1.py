class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)

        even = []
        odd = []
        for key in cnt.keys():
            num = cnt[key]
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        even.sort()
        odd.sort()

        return odd[-1] - even[0]