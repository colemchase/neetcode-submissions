class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # largest window with only two diff chars
        res = 0
        l = r = 0 
        basket = {}

        while r < len(fruits):
            basket[fruits[r]] = basket.get(fruits[r], 0) + 1 # add fruit to basket

            # decrement left most while basket is overflowing
            while len(basket.keys()) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            r+=1
            res = max(res, r-l)
        
        return res