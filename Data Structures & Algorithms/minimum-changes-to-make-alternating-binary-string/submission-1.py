class Solution:
    def minOperations(self, s: str) -> int:
        odd = 0
        for i in range(1, len(s), 2):
            if s[i] != "1":
                odd+=1
            if s[i-1] != "0":
                odd+=1
        if len(s) % 2 == 1:
            if s[-1] == "1":
                odd+=1

        even = 0
        for i in range(1, len(s), 2):
            if s[i] != "0":
                even+=1
            if s[i-1] != "1":
                even+=1
        if len(s) % 2 == 1:
            if s[-1] == "0":
                even+=1

        return min(odd, even)