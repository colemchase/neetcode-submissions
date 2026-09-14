class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + ","
        
        res += "#"
        for s in strs:
            res+=s

        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        if s == "":
            res.append("")
            return res

        i = 0
        j = i
        k = s.index("#")+1
        while s[i] != "#": # process all the words

            while s[j] != ",": # grab the length of current word
                j+=1
            curr_length = int(s[i:j])
            res.append(s[k:k+curr_length])

            j += 1
            i = j
            k+=curr_length

        return res


    