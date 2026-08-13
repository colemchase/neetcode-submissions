class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "chaseyrooroo"
        return res
    def decode(self, s: str) -> List[str]:
        return [] if len(s) == 0 else s.split("chaseyrooroo")[:-1]
    