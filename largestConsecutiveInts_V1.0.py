import time
import sys
import random
import numpy as np

array = [2,3,4,6,8,9,10,11,12,14,15,16,19,23,36,37,-1,0,-2] #testcase

#q1= np.sort(testarray)
def consecIntsNP(array):
    #array = list(np.sort(array)) #why do i have to list the np.sort ?? data type is ndarray. maybe thats why.
    array = list(np.sort(array)) #seems to be approx twice as fast... interesting. maybe because i had to use list() to convert it. Find way without list?
    testcase = []
    x=0 #current value
    temp = 1 #next value
    tempx = 0 #placeholder to compare next to.
    while True:
        #for debugging use below#
        #print("x:" + str(x))
        #print("temp:" + str(temp))
        #print(len(array))
        if (array[temp]-array[tempx]==0): #what if theres 3 of the same numbers in a row ? to technically be the most robust I need a more sound method.
            array.remove(array[temp]) #temp will automatically then consider next value.
            if temp >= len(array): #if i have to remove a duplicate and that duplicate occurs at the last 2 of the array, then temp will be outve bounds.
                temp -= 1
        if abs(array[temp] - array[tempx]) != 1: #since sorted. checks next array next value vs current value.
            testcase.append(array[x:temp]) #if they're not within 1 adds the anything that was previously within 1 and updates x to index of value not within 1, temp to next, and tempx to x.
            x = temp
            tempx = temp
            temp += 1
            if temp == len(array): #incase temp hits maximum limit after finding that the last value and previous value are not within one and updating.
                testcase.append(array[x:temp])
                return testcase
        else: #if they're within one, moves the placeholder and temp to the next ones.
            temp += 1
            tempx += 1
            if temp == len(array): #incase temp hits limit while searching for consec ints.
                testcase.append(array[x:temp])
                return testcase

#this code is same as above but utilized python sorting algorithm instead of numpys default quick sorting
def consecIntsPY(array):
    array.sort()
    testcase = []
    x = 0
    temp = 1
    tempx = 0
    while True:
        # for debugging use below#
        # print("x:" + str(x))
        # print("temp:" + str(temp))
        # print(len(array))
        if (array[temp] - array[
            tempx] == 0):  # what if theres 3 of the same numbers in a row ? to technically be the most robust I need a more sound method.
            array.remove(array[temp])  # temp will automatically then consider next value.
            if temp >= len(
                    array):  # if i have to remove a duplicate and that duplicate occurs at the last 2 of the array, then temp will be outve bounds.
                temp -= 1
        if abs(array[temp] - array[tempx]) != 1:
            testcase.append(array[x:temp])
            x = temp
            tempx = temp
            temp += 1
            if temp == len(array):
                testcase.append(array[x:temp])
                return testcase
        else:
            temp += 1
            tempx += 1
            if temp == len(array):
                testcase.append(array[x:temp])
                return testcase

def consecIntsNP_HS(array):
    # array = list(np.sort(array)) #why do i have to list the np.sort ?? data type is ndarray. maybe thats why.
    array = list(np.sort(array,kind='heapsort'))
    testcase = []
    x = 0
    temp = 1
    tempx = 0
    while True:
        # for debugging use below#
        # print("x:" + str(x))
        # print("temp:" + str(temp))
        # print(len(array))
        if (array[temp] - array[
            tempx] == 0):  # what if theres 3 of the same numbers in a row ? to technically be the most robust I need a more sound method.
            array.remove(array[temp])  # temp will automatically then consider next value.
            if temp >= len(
                    array):  # if i have to remove a duplicate and that duplicate occurs at the last 2 of the array, then temp will be outve bounds.
                temp -= 1
        if abs(array[temp] - array[tempx]) != 1:
            testcase.append(array[x:temp])
            x = temp
            tempx = temp
            temp += 1
            if temp == len(array):
                testcase.append(array[x:temp])
                return testcase
        else:
            temp += 1
            tempx += 1
            if temp == len(array):
                testcase.append(array[x:temp])
                return testcase
#testing the code runtime by generating a small and big array. Then adding an array intended for inputting the runtime of 10 - 1000 runs in there and averaging it
#to determine the average runtime for small computations as well as large computations. Quicksort from numpy, heapsort from numpy, and python sorting alg are investigated.
#apparently python sorting alg is timsort, which is a hybrid of insertion + mergesort.
timenpQS_BC = []
timenpQS_WC = []
timepy_BC = []
timepy_WC = []
timenpHS_BC = []
timenpHS_WC = []
testarrayBC = [int(random.random() * 1000) for _ in range(10)]
testarrayWC = [int(random.random() * 20000) for _ in range(20000)]
for i in range(1,1000):
    print(i)
    start = time.clock()
    (consecIntsPY(testarrayBC))
    end = time.clock() - start
    timepy_BC.append(end)

for i in range(1,1000):
    print(i)
    start = time.clock()
    (consecIntsPY(testarrayWC))
    end = time.clock() - start
    timepy_WC.append(end)
for i in range(1,1000):
    print(i)
    start = time.clock()
    (consecIntsNP(testarrayBC))
    end = time.clock() - start
    timenpQS_BC.append(end)

for i in range(1,1000):
    print(i)
    start = time.clock()
    (consecIntsNP(testarrayWC))
    end = time.clock() - start
    timenpQS_WC.append(end)

for i in range(1,1000):
    print(i)
    start = time.clock()
    (consecIntsNP_HS(testarrayBC))
    end = time.clock() - start
    timenpHS_BC.append(end)
for i in range(1,1000):
    print(i)
    start = time.clock()
    (consecIntsNP_HS(testarrayWC))
    end = time.clock() - start
    timenpHS_WC.append(end)
#results arent making sense to me.
runtime_avgPYBC=sum(timepy_BC)/len(timepy_BC)
runtime_avgPYWC=sum(timepy_WC)/len(timepy_WC)
runtime_avgNPBC=sum(timenpQS_BC)/len(timenpQS_BC)
runtime_avgNPWC=sum(timenpQS_WC)/len(timenpQS_WC)
runtime_avgNP_HS_BC=sum(timenpHS_BC)/len(timenpHS_BC)
runtime_avgNP_HS_WC=sum(timenpHS_WC)/len(timenpHS_WC)

print("average best case average runtime using python sort :" +str(runtime_avgPYBC))
print("average worst case average runtime using python sort :" +str(runtime_avgPYWC))
print("average best case average runtime using np sort :" +str(runtime_avgNPBC))
print("average worst case average runtime using np sort :" +str(runtime_avgNPWC))
print("average best case average runtime using np heap sort :" +str(runtime_avgNP_HS_BC))
print("average worst case average runtime using np heap sort :" +str(runtime_avgNP_HS_WC))
print("pysort % faster by approximately: "+str(runtime_avgNPBC/runtime_avgPYBC)+"x in bestcase performance")
print("pysort % faster by approximately: "+str(runtime_avgNPWC/runtime_avgPYWC)+"x in worstcase performance")
print("numpy quicksort % faster than hsort by approximately: "+str(runtime_avgNPBC/runtime_avgNP_HS_BC)+"x in bestcase performance")
print("numpy quicksort % faster than hsort by approximately: "+str(runtime_avgNPWC/runtime_avgNP_HS_WC)+"x in worstcase performance")