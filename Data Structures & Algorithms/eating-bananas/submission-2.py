class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low, high = 1, piles[-1]
        res = piles[-1]

        while low <= high:
            mid = low + (high-low) // 2
            
            rem = h
            for num in piles:
                temp = num // mid
                temp += 1 if num % mid != 0 else 0
                rem -= temp
            print("rem: " + str(rem))
            if rem >= 0: # eating too fast
                high = mid - 1  
                res = min(res, mid)  
                print("here")
            elif rem < 0: # not enough bite
                low = mid + 1

        return res