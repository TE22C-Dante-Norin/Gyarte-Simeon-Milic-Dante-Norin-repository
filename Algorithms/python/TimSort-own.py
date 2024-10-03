import time
start_time = time.time()
import random
import math

numbers = 100000
minRunSize = 16
listToSort = []

def InsertionSort(list):
    sortedList = []
    sortedList.append(list[0])
    for i in range(len(list) - 1):
        index = 0
        while(True):
            if(index > len(sortedList)-1):
                sortedList.append(list[i+1])
                break
            elif(sortedList[index] > list[i+1]):
                sortedList.insert(index, list[i+1])
                break
            else:
                index += 1
    return sortedList

def merge(list1,list2):
    index1 = 0
    index2 = 0
    mergedList = []
    for i in range(len(list1)+len(list2)):
        if(list1[index1] < list2[index2]):
            mergedList.append(list1[index1])
            index1 += 1
            if(index1 > len(list1) - 1):
                for j in range(len(list2)-index2):
                    mergedList.append(list2[j+index2])
                break
        else:
            mergedList.append(list2[index2])
            index2 += 1
            if(index2 > len(list2) - 1):
                for j in range(len(list1)-index1):
                    mergedList.append(list1[j+index1])
                break
    return mergedList

for i in range(numbers):
    listToSort.append(random.randint(0,100))

runList = []
tempList = []
for i in range(math.floor(len(listToSort)/minRunSize)):
    runList.append([])
    for j in range(minRunSize):
        runList[i].append(listToSort[j + i*minRunSize])
if((len(listToSort) % minRunSize) != 0):
    runList.append([])
    for i in range(len(listToSort)-(math.floor(len(listToSort)/minRunSize)*minRunSize)):
        runList[len(runList)-1].append(listToSort[i + (math.floor(len(listToSort)/minRunSize)*minRunSize)])

for i in range(len(runList)):
    runList[i] = InsertionSort(runList[i])

while(len(runList) > 1):
    for i in range(math.floor(len(runList)/2)):
        tempList.append(merge(runList[i*2],runList[i*2 + 1]))
    runList.clear()
    for i in range(len(tempList)):
        runList.append(tempList[i])
    tempList.clear()
sortedList = runList[0]
print("Process finished --- %s seconds ---" % (time.time() - start_time))