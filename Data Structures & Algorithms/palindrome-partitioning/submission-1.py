class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        subset = list(s)

        def backtrack(subset, i):
            if i >= len(subset)-1:
                for word in subset:
                    if word != word[::-1]:
                        return
                res.append(subset.copy())
        
                return
            
            # can i merge into a palindrome?
            if i+1 < len(subset):
                temp = subset[i] + subset[i+1]
                left = subset[i]
                subset[i] = temp
                right = subset.pop(i+1)
                backtrack(subset, i)
                subset.insert(i+1, right)
                subset[i] = left


            # lets not merge
            backtrack(subset, i+1)

        backtrack(subset, 0)

        return res
