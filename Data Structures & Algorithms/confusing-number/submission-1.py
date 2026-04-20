class Solution:
    def confusingNumber(self, n: int) -> bool:
        # if you can rotate it and its a new number ur good
        res = ""

        for c in str(n):
            if c in "23457":
                return False
            
            match c:
                case "6":
                    res+="9"
                case "9":
                    res+="6"
                case _:
                    res+=c

        return int(res[::-1]) != n