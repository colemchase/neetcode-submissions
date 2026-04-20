class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rot = {"0":"0", "1":"1","8":"8", "6":"9", "9":"6"}

        l = 0
        r = len(num)-1
        while l<=r:
            if num[l] not in rot or num[r] != rot[num[l]]:
                return False

            l+=1
            r-=1

        return True