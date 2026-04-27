class Solution:
    def simplifyPath(self, path: str) -> str:
        
        paths = path.split("/")
        p = []
        for x in paths: # remove double slashes
            if x == "/" and len(p) > 0 and p[-1] == "/":
                continue
            p.append(x)
        
        paths = []
        for x in p: # remove blanks
            if x != "":
                paths.append(x)
        
        stack = []
        for p in paths:
            match p:
                case "..":
                    if len(stack) > 0:
                        stack.pop()
                case ".":
                    continue
                case _:
                    stack.append(p)

        res = "/" if len(stack) == 0 else ""
        for item in stack:
            res += "/" + item

        return res