class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chcnt = Counter(chars)
        res = 0
        for word in words:
            wcnt = Counter(word)
            valid = True
            for key in wcnt.keys():
                if key in chcnt:
                    if wcnt[key] > chcnt[key]:
                        valid = False
                else:
                    valid = False
            if valid:
                res+=len(word)
        return res