class Solution:
    def findPermutation(self, s: str) -> List[int]:

        # DDDDDDDI
        # 123456789
        # 876543219
        res = [i for i in range(1, len(s)+2)]

        def reverse(i, j):
            while i < j:
                temp = res[j]
                res[j] = res[i]
                res[i] = temp
                i += 1
                j -= 1

        i = 0
        while i < len(s):
            if s[i] == "D":
                # reverse
                j = i 
                while j < len(s) and s[j] == "D":
                    j+=1
                reverse(i, j)
                i = j
            else:
                i+=1


        return res
