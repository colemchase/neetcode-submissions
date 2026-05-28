class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                curr = money - prices[i] - prices[j]
                if curr >= 0:
                    return curr
        
        return money