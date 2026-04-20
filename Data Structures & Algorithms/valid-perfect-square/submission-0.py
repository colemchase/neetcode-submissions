class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # find the largest number than when squared is <= num
        # if equal return true
        # return false

        # bs from 1 to num.    gives logn runtime


        l, r = 1, num

        while l <= r:

            if l == r:
                return l**2 == num

            mid = (l+r) // 2

            curr = mid**2
            
            if curr < num:
                l = mid + 1
            elif curr > num:
                r = mid - 1
            else:
                return True
        
        return False

