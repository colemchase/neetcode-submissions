class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        stacy = set()
        for sp in similarPairs:
            stacy.add((sp[0], sp[1]))
            stacy.add((sp[1], sp[0]))
        
        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i]:
   
                if (sentence1[i], sentence2[i]) not in stacy:
                    return False
        
        return True
