import random
def CountingSort(digitArray):
    maxValue = GetMaxValue(digitArray)
    countingArray = []
    for i in range(maxValue + 2):
        countingArray.append(0)
    for i in range(len(digitArray)):
        countingArray[digitArray[i]] += 1
    sortedDigitArray = []
    for i in range(maxValue + 1):
        while countingArray[i] > 0:
            sortedDigitArray.append(i)
            countingArray[i] -= 1
    print(sortedDigitArray)
        
def GetMaxValue(array):
    tempMaxValue = 0
    for i in range(len(array)):
        if(array[i] > tempMaxValue):
            tempMaxValue = array[i]
    return tempMaxValue
    


arrayToSort = []
for i in range(100000):
    arrayToSort.append(random.randint(0,9))

CountingSort(arrayToSort)