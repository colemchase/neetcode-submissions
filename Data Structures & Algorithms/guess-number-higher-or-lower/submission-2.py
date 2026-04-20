# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l , h = 1, n
        while l <= h:
            if l == h:
                return l
            
            mid = (h + l) // 2

            g = guess(mid)

            if g == -1:
                h = mid - 1
            elif g == 1:
                l = mid + 1
            else:
                return mid
        

        

            
            