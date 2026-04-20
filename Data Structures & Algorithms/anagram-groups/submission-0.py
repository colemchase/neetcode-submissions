class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through the strings
        # compare to each anagram groups first anagram
        # if matching, append the anagram to the respective group
        # if no matches found (end of anagram groups list) add to new group
        def isAna(curr, cmp):
            hm = {}
            for c in curr:
                if c not in hm:
                    hm[c] = 0
                hm[c] += 1
            for c in cmp:
                if c not in hm:
                    return False
                hm[c]-=1
            for k in hm.keys():
                if hm[k] != 0:
                    return False
            return True
        
        res = []
        for s in strs:
            for i in range(len(res)+1):
                if i == len(res):
                    res.append([s])
                    break
                cmp = res[i][0]
                if isAna(s, cmp):
                    res[i].append(s)
                    break

        return res

            