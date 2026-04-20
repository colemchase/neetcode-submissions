class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        res = set(mat[0])
        for m in mat[1:]:
            res = res & set(m)
        
        return sorted(res)[0]