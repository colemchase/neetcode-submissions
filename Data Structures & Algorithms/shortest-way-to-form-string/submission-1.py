class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i = 0

        res = 1
        stacy = set(source)
        for c in target:
            if c not in stacy:
                return -1
            flag = True
            while flag:
                if i == len(source):
                    i = 0
                    res+=1
                curr = source[i]
                if curr == c:
                    flag = False
                i+=1


        return res