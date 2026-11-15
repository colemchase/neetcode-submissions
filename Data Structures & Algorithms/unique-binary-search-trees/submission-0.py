class Solution:
    def numTrees(self, n: int) -> int:
        
        numTree = [1] * (n+1)

        for nodes in range(2, n+1):
            curSum = 0
            for i in range(1, nodes+1):
                left = i - 1
                right = nodes - i
                curSum += numTree[left] * numTree[right]
            numTree[nodes] = curSum

        return numTree[n]  

