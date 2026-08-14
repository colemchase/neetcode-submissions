class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Naive clear out the strings unless alnum

        # Optimal
        # Two Pointer

        l = 0
        r = len(s)-1

        # Try to catch inequal chars while l and r get closer and closer
        s = s.lower()
        while l < r:
            # skip 
            if not s[l].isalnum(): 
                l += 1
                continue
            if not s[r].isalnum():
                r -=1
                continue
                
            # valid alphabet or numeric
            if not s[l] == s[r]:
                    return False
            l += 1
            r -= 1
        
        return True