class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ms = []
        res = []
        for temp in temperatures[::-1]:
            curr = 0
            while len(ms) != 0:
                curr+=1
                if ms[-1] <= temp:
                    ms.pop()
                else:
                    break
            if len(ms) == 0:
                curr = 0
            if curr > 1:
                ms+=[temp]*curr
            else:
                ms.append(temp)
            res.append(curr)
                
        
        return res[::-1]