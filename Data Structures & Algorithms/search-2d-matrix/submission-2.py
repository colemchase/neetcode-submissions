class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # make a binary search function 

        # find row where item is first and return, or find largest row under the number

        l, r = 0, len(matrix) - 1
        row = 0
        while l <= r: # search through rows

            if l == r: # last option
                if matrix[l][0] < target:
                    row = l 
                elif matrix[l][0] > target:
                    row = l - 1
                else:
                    return True
                
            mid = (r+l) // 2
            head = matrix[mid][0]
            if head > target: # row is too high
                r = mid - 1
            elif head < target: # could be in this row, record it and move higher
                row = max(row, mid)
                l = mid + 1
            else: # you found target without searching through columns
                return True
            

        l, r = 0, len(matrix[0]) - 1

        while l <= r: # search through columns
            if l == r:
                return matrix[row][l] == target
            
            mid = (r+l) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False
