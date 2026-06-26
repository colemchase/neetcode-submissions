class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []

        i = 0
        highest = 0
        while i < len(heights):
            j = len(heights)-i-1
            curr = heights[j]
            if curr > highest:
                highest = curr
                res.append(j)
            i+=1

        return res[::-1]
