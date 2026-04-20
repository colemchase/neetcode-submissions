class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        winner = float('-inf')
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = winner
            winner = max(winner, temp)
        arr[-1] = -1
        return arr