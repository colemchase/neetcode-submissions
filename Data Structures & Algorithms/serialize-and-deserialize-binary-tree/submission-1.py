# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # no need to keep a class state. unit tests passes serialize to the deserializ

    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # turn the tree into an arr of values
        # append the int val 
        # or append a "N" for null
        res = []

        def dfs(curr):
            if not curr:
                res.append("N")
                return 
            res.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return ",".join(res)
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # turn str into arr, move through array, build tree
        arr = data.split(",")
        
        # global accessible i for current index in arr
        # dfs through the arr, like how we built it
        self.i = 0
        def dfs():
            if arr[self.i] == "N":
                self.i+=1
                return None
            curr = TreeNode(int(arr[self.i]))
            self.i+=1
            curr.left = dfs()
            curr.right = dfs()
            return curr
        return dfs()



        
