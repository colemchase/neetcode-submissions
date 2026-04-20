class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stacy = []

        for o in operations:
            print(stacy)
            match o:
                case "+":
                    stacy.append(stacy[-1] + stacy[-2])
                case "D":
                    stacy.append(stacy[-1] * 2)
                case "C":
                    stacy.pop()
                case _:
                    stacy.append(int(o))
        
        return sum(stacy)