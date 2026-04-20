class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        
        def recurse(a):

            temp = []
            temp.append(a[0])

            for i in range(1, len(a)-1):
                if a[i] > a[i-1] and a[i] > a[i+1]:
                    temp.append(a[i]-1)
                elif a[i] < a[i-1] and a[i] < a[i+1]:
                    temp.append(a[i]+1)
                else:
                    temp.append(a[i])

            temp.append(a[-1])

            return recurse(temp) if a != temp else temp
        
        return recurse(arr)