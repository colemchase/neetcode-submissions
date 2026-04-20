class Solution:

    def reverse(self, arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l+1, r-1
        
    def reverseWord(self, arr):
        n = len(arr)
        i = j = 0
        while i < n:
            while j < n and arr[j] != " ":
                j+=1
            self.reverse(arr, i, j-1)
            i=j+1
            j+=1
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        self.reverse(s, 0, len(s)-1)
        self.reverseWord(s)
