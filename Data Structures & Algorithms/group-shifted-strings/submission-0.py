class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = []
        for i, curr in enumerate(strings):
            flag = False
            for j in range(len(res)):
                g = res[j][0]
                for k in range(26):
                    cmp = ""
                    for c in curr:
                        c = ord(c)
                        if c+k > 122:
                            cmp+=chr(((c+k)%123)+97)
                        else:
                            cmp+=chr(c+k)
                    if cmp == g:
                        res[j].append((strings[i]))
                        flag = True
                        break
                if flag:
                    break
            if not flag:
                res.append([curr])
        
        return res