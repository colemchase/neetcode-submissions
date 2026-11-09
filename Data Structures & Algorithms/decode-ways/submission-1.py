class Solution:
    def numDecodings(self, s: str) -> int:
        hm = {}
        
        def parse(i):
            print(i)
            if i in hm:
                return hm[i]

            res = 0
            if i >= len(s):
                if i == len(s):
                    return 1
                return res
            
            # parse 2 chars
            if i < len(s)-1:
                if s[i] != "0" and int(s[i:i+2]) <= 26:
                    res += parse(i+2)

            # parse 1 char
            if i < len(s):
                if s[i] != "0":
                    res += parse(i+1)
            hm[i] = res
            return hm[i]

        parse(0)
        
        return hm[0]
            


        
        