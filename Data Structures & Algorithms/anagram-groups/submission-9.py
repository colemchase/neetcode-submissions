class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Obective: group strs into anagram groups (same counts of letters)

        # Naive: make a group, comp curr to all words in group
        # Optimal: Dont use Counter, sort the strs 
        
        # sorted_word -> [word, word1, word2]
        hm = {}   
        for word in strs:
            curr = list(word)
            curr.sort()
            curr = "".join(curr)
            if curr not in hm:
                hm[curr] = []
            hm[curr].append(word)
        return list(hm.values())
        

            