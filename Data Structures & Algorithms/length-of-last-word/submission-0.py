class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")[::-1]
        for x in s:
            if len(x) != 0:
                return len(x)
