class StockSpanner:

    def __init__(self):
        self.stx = []


    def next(self, price):
        # how long ago was the next highest price?
        # stack will have the lowest price and the number of 
        res = 1
        if len(self.stx) == 0:
            self.stx.append((price, res))
            return res
        i = len(self.stx)-1
        while i >= 0:
            prev_price, prev_score = self.stx[i]
            if prev_price <= price:
                res += prev_score
                i -= prev_score
            else:
                break
        self.stx.append((price, res))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)