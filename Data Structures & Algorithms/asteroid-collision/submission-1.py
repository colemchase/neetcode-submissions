class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stacy = []

        for a in asteroids:
            if a > 0: # pos 
                stacy.append(a)
            else: # neg
                survive = True
                while len(stacy) > 0 and stacy[-1] > 0: # collide till resolution
                    if abs(a) <= stacy[-1]: # curr neg smaller than next pos
                        survive = False
                        if abs(a) == stacy[-1]: # curr neg eqaul next pos
                            stacy.pop()
                        break
                    stacy.pop() # curr neg bigger than next pos
                if survive:
                    stacy.append(a)
                    
                
        return stacy