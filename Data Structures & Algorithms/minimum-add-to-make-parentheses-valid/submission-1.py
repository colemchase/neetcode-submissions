class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        errors = 0
        for c in s:
            if c == "(":
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    errors += 1
                    balance += 1
            
        
        return balance + errors
