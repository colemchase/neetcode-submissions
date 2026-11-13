class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()
        res = float('inf')
        low = 1
        high = piles[-1]

        # binary search for min eat val to eat all piles in h hours
        while low <= high:
            eat = ((high-low) // 2) + low # eat per hour
            hours = 0
            for i in range(len(piles)): # eat each pile
                hours += piles[i] // eat
                hours += 1 if piles[i] % eat != 0 else 0

            if hours <= h:
                res = min(res, eat)
                high = eat - 1
            else:
                low = eat + 1

        return res