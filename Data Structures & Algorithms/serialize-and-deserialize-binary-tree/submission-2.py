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
        if not root:
            return ""
        self.res = ""
        def dfs(curr):
            if curr:
                self.res += str(curr.val) + "#"
                dfs(curr.left)
                dfs(curr.right)
            else:
                self.res += "N" + "#"
        dfs(root)
        return self.res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        self.i = 0
        data = data.split("#")
        print(data)

        def dfs():
            if self.i < len(data):
                if data[self.i] == "N":
                    self.i+=1
                    return None
                curr = TreeNode(int(data[self.i]))
                self.i+=1
                curr.left = dfs()
                curr.right = dfs()
                return curr

        return dfs()
        

        
