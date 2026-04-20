class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict

    def shortest(self, word1: str, word2: str) -> int:
        i1 = -1
        i2 = -1
        res = len(self.wordsDict)
        for i in range(len(self.wordsDict)):
            if self.wordsDict[i] == word1:
                i1 = i
            elif self.wordsDict[i] == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                    res = min(res, abs(i1-i2))
                    print(res)
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
