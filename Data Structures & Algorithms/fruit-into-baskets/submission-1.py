class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window
        basket = {} # fruit_type, count
        left = 0
        right = 0
        res = 0

        while right < len(fruits):
            # add fruit at right
            fruit = fruits[right]
            if fruit not in basket:
                basket[fruit] = 0
            basket[fruit] += 1

            # drop fruits at left while we are overflowing
            while len(basket.keys()) > 2:
                fruit = fruits[left]
                basket[fruit] -= 1
                if basket[fruit] == 0:
                    del basket[fruit]
                left += 1

            right += 1
            res = max(res, right-left)

        return res