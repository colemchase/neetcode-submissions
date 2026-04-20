# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        # side that is larger sum than it should be holds the number

        l, r = 0, reader.length()-1

        while l <= r:
            if l == r:
                return l
                
            mid = (r+l) // 2
    
            if (r-l+1) % 2 == 1: # sides can be equal size, if equal return mid, else do mid + 1 or mid - 1
                if reader.length() == 1:
                    return mid
                curr = reader.compareSub(l, mid-1, mid+1, r)
                if curr == 0:
                    return mid
                elif curr == 1:
                    r = mid-1
                elif curr == -1:
                    l = mid + 1
            else:
                # check inner two
                inner = reader.compareSub(mid, mid, mid+1, mid+1)

                if inner == 1:
                    return mid
                elif inner == -1:
                    return mid+1
            
                curr = reader.compareSub(l, mid-1, mid+2, r)
                if curr == 1:
                    r = mid-1
                elif curr == -1:
                    l = mid+2
                
            


