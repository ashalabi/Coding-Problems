# Find Pair with Given Sum in the Array
# Input : arr = 8 7 2 5 3 1, sum = 10. Output : pair found at index 0 and 2 (8+2) or @ 1 and 4.
import time


def sumArray(array, sum):
    array.sort()
    high = len(array) - 1
    i = 0

    while (i < high):
        if (array[i] + array[high] == sum):
            print("pair found at: " + str(i) + ", " + str(high) + ".")
            # assuming no duplicates can just decrement or increment high low
            high -= 1

        if (array[i] + array[high] < sum):
            i += 1
        if (array[i] + array[high] > sum):
            high -= 1

    #can try to improve this by returning the actual values to be used in something else instead of returning the list :S
    return array

def sumArrayDictionary(array, sum):
    y = list(array)
    map = dict(zip(y, array))
    for x in array:
        key = sum - x
        if key in map:
            return key

arr = [8, 7, 2, 5, 3, 1]
sum = 10
start = time.clock()
x = sumArray(arr, 10)
print(x)
print(time.clock() - start)

# next via hash map ?
start2 = time.clock()
y = sumArrayDictionary(arr,sum)
print(y)
print(time.clock()-start2)
