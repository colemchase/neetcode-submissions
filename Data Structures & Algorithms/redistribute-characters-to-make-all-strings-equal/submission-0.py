class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        s = ""
        for word in words:
            s+=word
    
        cnt = Counter(s)
        for key in cnt.keys():
            if cnt[key] % len(words) != 0:
                return False

        return True