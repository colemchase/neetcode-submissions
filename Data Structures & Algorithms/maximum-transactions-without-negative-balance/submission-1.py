class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        res = 0
        balance = 0
        for t in transactions:
            if balance + t >= 0:
                balance += t
                res += 1
        return res