import time
import sys

#sort binary array with linear time constant space.
#try to come up with a second method tomorrow.
def sortBinArray(binaryArray): #assuming its a binary array. #constant space since no variables are defined in loop.
    ones = binaryArray.count(1) #count is a O(n) so linear space
    zeros = binaryArray.count(0)
    set_zero = [0]*zeros
    set_ones = [1]*ones
    binaryArray = set_zero+set_ones
    return binaryArray

testArray = [1, 1, 0, 1, 1, 0, 0, 1 , 0 , 1, 1, 0, 1, 0]
start = time.clock()
print(sortBinArray(testArray))
end = time.clock()-start
print(end)
print(sys.getsizeof(sortBinArray(testArray)))