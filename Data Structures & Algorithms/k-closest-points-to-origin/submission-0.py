class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        
        for i, point in enumerate(points):
            distances.append( ( ( point[0]**2 + (point[1])**2 ) **(1/2) , i))

        distances.sort(key=lambda x: x[0])

        res = []
        for dist, i in distances[:k]:
            res.append(points[i])

        return res
