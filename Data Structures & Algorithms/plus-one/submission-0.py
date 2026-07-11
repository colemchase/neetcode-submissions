class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        while i >= 0:
            if digits[i] == 9 and carry:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += carry
                carry = 0
            i-=1
        
        if digits[0] == 0 and carry:
            digits = [1] + digits
        
        return digits