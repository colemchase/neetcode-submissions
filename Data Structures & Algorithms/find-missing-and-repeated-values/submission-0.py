class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        cnt = {}
        n = len(grid)
        for row in grid:
            for item in row:
                if item not in cnt:
                    cnt[item] = 0
                cnt[item] +=1
        

        res = [0, 0]
        for i in range(1, (n*n)+1):
            if i in cnt:
                if cnt[i] == 2:
                    res[0] = i
            else:
                res[1] = i

        return res