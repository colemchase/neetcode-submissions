class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            word = words[i]
            for j in range(len(words)):
                if j != i:
                    if word not in res:
                        if word in words[j]:
                            res.append(word)
        return res