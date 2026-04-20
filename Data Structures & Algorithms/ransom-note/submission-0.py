class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = Counter(magazine)
        for c in ransomNote:
            if c not in cnt:
                return False
            cnt[c] -= 1
            if cnt[c] < 0:
                return False
        return True