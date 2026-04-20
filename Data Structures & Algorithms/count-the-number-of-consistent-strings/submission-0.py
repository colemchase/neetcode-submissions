class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for word in words:
            flag = True
            for c in set(word):
                if c not in allowed:
                    flag = False
            res += 1 if flag else 0
        return res 