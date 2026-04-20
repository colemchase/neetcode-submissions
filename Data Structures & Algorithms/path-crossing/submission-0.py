class Solution:
    def isPathCrossing(self, path: str) -> bool:
        stacy = set()
        stacy.add((0, 0))
        x = 0
        y = 0
        for p in path:
            match p:
                case "N":
                    y+=1
                case "E":
                    x+=1
                case "S":
                    y-=1
                case "W":
                    x-=1
            curr = (x, y)
            print(curr)
            if curr not in stacy:
                stacy.add(curr)
            else:
                return True
        return False