class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for s in strs[1:]:
            while res not in s:
                res = res[:len(res)-1]
                
        return res