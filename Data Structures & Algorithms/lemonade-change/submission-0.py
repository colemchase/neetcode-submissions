class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        bank = {}
        bank[5] = 0
        bank[10] = 0
        bank[20] = 0

        for bill in bills:
            bank[bill] += 1
            change = bill - 5
            if change == 10:
                if bank[10] > 0:
                    bank[10] -= 1
                    continue
                if bank[5] > 1:
                    bank[5] -= 2
                    continue 
                return False

            if change == 15:
                if bank[10] > 0:
                    if bank[5] > 0:
                        bank[10] -= 1
                        bank[5] -= 1
                        continue
                if bank[5] > 2:
                    bank[5] -= 3
                    continue
                return False

            if change == 5:
                if bank[5] > 0:
                    bank[5] -= 1
                    continue
                return False
                

            
        return True