import time
import sys
from collections import defaultdict


def duplicate(array):
    y = len(array)
    x = list(array)
#    for i in range(0,y+1):
#        x.append(i)
    test = list(array)
    map1 =  defaultdict(list)
    for k, v in zip(x, array):
        map1[k].append(v)
    return map1

def duplicate2(array):
    out = {}
    dup = {}
    true = {}
    #duplicateMap = {} to be used if sorted.
    for i in range(0,len(array)): #i want to be able to just go from 1 to # of items and associate a value with that index. then check if the VALUE is in there, not check by index in dictionary.
        v = array[i]

        if i>=1 and v in out:#v == array[i-1], will work if sorted. Without sorting though, use value in map, and dont return the index. Mayhbe later get it better.
           dup.append(array[i])
           # print("Duplicate found at index location "+str(i-1)+" and "+str(i)+".")
           # duplicateMap.update({i-1:i})
        out.update({str(i):v})
    return out, dup, true

def duplicate3(array):
    dup = set()
    nDup = set()
    for i in array:
        if i in nDup:
            dup.add(i)
        else:
            nDup.add(i)
    return nDup, dup

#DUPLICATE 4:
#another method, make a set out of array. Iterate over the set, removing each element in set from array. Anything left in array is a duplicate.

#this seems to usually be the fastest :D
def duplicate4(array):
    unique = set(array)
    newArray = list(array)
    for x in unique:
       # print("this will be removed "+str(x)+" of data type: "+str(type(x)))
        newArray.remove(x)
    return unique#, set(newArray) #setted it just so that both are returned as the same datatypes.

y = ["testing","testing","tea"] #bug. seems that if i put any non repeated value from 0-6 it still flags that there is a repeated element since it is in the index.
#need to add in duplicate test, so far so good tho.
start = time.clock()
print(duplicate(y))
end = time.clock() - start
print(end)
print(sys.getsizeof(duplicate(y)))

start2 = time.clock()
print(duplicate2(y))
end2 = time.clock() - start2
print(end2)
print(sys.getsizeof(duplicate2(y)))

start3 = time.clock()
print(duplicate3(y))
end3 = time.clock() - start3
print(end3)
print(sys.getsizeof(duplicate3(y)))

start4 = time.clock()
print(duplicate4(y))
end4 = time.clock() - start4
print(end4)
print(sys.getsizeof(duplicate4(y)))