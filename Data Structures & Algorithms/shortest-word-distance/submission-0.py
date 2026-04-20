class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1 = -1
        i2 = -1
        res = len(wordsDict)
        
        for i in range(len(wordsDict)):
            num = wordsDict[i]
            if num == word1:
                i1 = i
            elif num == word2:
                i2 = i
            
            if i1 != -1 and i2 != -1:
                res = min(res, abs(i1-i2))
        
        return res

