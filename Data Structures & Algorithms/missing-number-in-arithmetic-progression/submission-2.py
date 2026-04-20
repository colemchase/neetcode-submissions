class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if arr[0] > arr[-1]:
            arr = arr[::-1]
        
        prev = arr[0]
        jump = arr[1] - arr[0]
        for num in arr[1:]: # assuming the first one is not it
            if num > prev + jump:
                return prev + jump
            elif num < prev + jump: # 2 6 8
                return prev - (num - prev)
            prev = num
        
        return arr[0]

