class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for key in cnt.keys():
            if cnt[key] == 1:
                return s.index(key)
        return -1