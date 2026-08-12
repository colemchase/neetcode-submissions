class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Obective: group strs into anagram groups (same counts of letters)

        # Naive: make a group, comp curr to all words in group

        # cmp curr word to first word in solved groups, if end of group, make a new group with the curr word
        hm = {}
        for word in strs:
            curr = [c for c in word]
            curr.sort()
            curr = "".join(curr)
            if curr not in hm:
                hm[curr] = []
            hm[curr].append(word)
        
        res = []

        for key in hm.keys():
            res.append(hm[key])

        return res

            