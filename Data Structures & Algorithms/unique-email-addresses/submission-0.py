class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        # dont count dots before the @

        # at least one char before the .com

        def validity(s):
            mid = s.index("@")
            l = s[:mid]
            d = s[mid+1:]

            # validate local section
            local = ""
            for c in l:
                if c == "+":
                    break
                if c != '.':
                    local+=c
            
            # validate domain section
            return (local, d)


        stacy = set()
        for email in emails:
            local, d = validity(email)
            email = local + "@" + d
            stacy.add(email)
        
        return len(stacy)