class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        hm = {}
        i = 0
        if len(words) != len(pattern):
            return False
        for word in words:
            p = pattern[i]
            if p not in hm and word not in hm: # new valid match
               hm[p] = word
               hm[word] = p
            else:
                if p not in hm or word not in hm:
                    return False
            i+=1
        return True
