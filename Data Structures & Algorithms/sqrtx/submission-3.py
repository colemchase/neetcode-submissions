class Solution:
    def mySqrt(self, x: int) -> int:
        # bs for the sqrt on the range of 1 to x
        # if not equal, return the highest sqrted num < x

        l, r = 1, x

        if not x:
            return 0

        res = 1
        while l <= r:
            if l == r:
                if l ** 2 <= x:
                    return l
                break
            
            mid = (l+r) // 2
            curr = mid**2
            print(mid)
            if curr < x:
                res = max(res, mid)
                l = mid + 1
            elif curr > x:
                r = mid - 1
            else:
                return mid
        return res

