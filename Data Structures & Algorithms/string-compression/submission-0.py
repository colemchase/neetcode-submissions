class Solution:
    def compress(self, chars: List[str]) -> int:
        
        res = ""

        l = 0
        while l < len(chars):
            curr = chars[l]
            r = 1
            while l+r < len(chars):
                if chars[l+r] == curr:
                    r+=1
                else:
                    break
            res += curr if r < 2 else curr + str(r)
            l+=r
        chars[:len(res)] = res
        return len(res)