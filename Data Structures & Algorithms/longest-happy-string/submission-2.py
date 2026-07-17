class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        
        letters = []
        if a:
            letters.append((-a, "a"))
        if b: 
            letters.append((-b, "b"))
        if c:
            letters.append((-c, "c"))
        if not len(letters):
            return ""

        heapq.heapify(letters)
        count, letter = heapq.heappop(letters)
        res += letter
        count += 1
        if count != 0:
            heapq.heappush(letters, (count, letter))
        
        if len(letters) > 0:
            count, letter = heapq.heappop(letters)
            res += letter
            count += 1
            if count != 0:
                heapq.heappush(letters, (count, letter))

        while len(letters) > 0:
            
            if letters[0][1] == res[-1] and letters[0][1] == res[-2]:
                if len(letters) == 1: # only letter left is wrong
                    return res
                # second choice is valid
                temp = heapq.heappop(letters)
                curr_count, curr_letter = heapq.heappop(letters)
                curr_count += 1
                res += curr_letter
                if curr_count != 0:
                    heapq.heappush(letters, (curr_count, curr_letter))
                heapq.heappush(letters, temp)
            else: # first letter possible is valid
                curr_count, curr_letter = heapq.heappop(letters)
                curr_count += 1
                res += curr_letter
                if curr_count != 0:
                    heapq.heappush(letters, (curr_count, curr_letter))

        return res