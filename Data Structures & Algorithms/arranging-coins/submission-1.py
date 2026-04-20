class Solution:
    def arrangeCoins(self, n: int) -> int:
        #
        ##
        ###
        ####
        ##### (n(n+1))/2

        # find highest number that is <= n when plugged into the math formula

        l = 1
        r = n

        res = 1
        
        while l <= r:
            mid = (l+r)//2
            
            curSum = (mid*(mid+1)) // 2
            
            if curSum == n:
                return mid

            if curSum < n:
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        
        return res



