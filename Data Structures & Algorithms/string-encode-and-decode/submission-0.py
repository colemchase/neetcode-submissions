class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        password = "chaseyrooroo"

        for s in strs:
            res+=s+password
            
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        password = "chaseyrooroo"

        while len(s) > 0:
            i = s.index(password)
            res.append(s[:i])
            s = s[i+len(password):]
           
        return res
    