#importerar random modulen för att kunna generera slumpmässiga tal till listan
import random

#Definerar functionen som skjöter hela sorteringen av listan, den använder flera andra mindre funktioner i sig
def RandixSort(radixArray):
    1 = 1



#Definerar en funktion för countingsort-algoritmen vilket används inom randixsort algoritmen 
def CountingSort(digitArray):
    #Tar fram det högsta värdet i listan
    maxValue = GetMaxValue(digitArray)
    #Definerar en temporär lista för att räkna hur många av varje element som finns och lägger till nollor för varje element upp till maxvärdet som togs fram innan
    countingArray = []
    for i in range(maxValue + 2):
        countingArray.append(0)
    #En loop som går igenom hela listan och räknar hur många som finns av varje element
    for i in range(len(digitArray)):
        countingArray[digitArray[i]] += 1
    #Definerar en lista som de sorterade värdena ska hämna i
    sortedDigitArray = []
    #Loop som går igenom countingArray listan och lägger till siffrorna i den nya listan i rätt ordning
    for i in range(maxValue + 1):
        while countingArray[i] > 0:
            sortedDigitArray.append(i)
            countingArray[i] -= 1
    #returnerar den sorterade listan
    return sortedDigitArray

#Definerar en funktion som tar reda på det högsta värdet i en lista    
def GetMaxValue(array):
    #Börjar med att sätta högsta hittade värdet till 0
    tempMaxValue = 0
    #Sen går igenom listan och varje gång den hittar ett högre nummer sparar den det numret som högsta hittade värde
    for i in range(len(array)):
        if(array[i] > tempMaxValue):
            tempMaxValue = array[i]
    #returnerar högsta värdet i listan
    return tempMaxValue

#Definerar en funktion för att ta ut en specifik siffra från ett längre tal
def get_digit(number, n):
    return number // 10**n % 10
    
#Definerar en funktion för att slumpa fram en osorterad lista
def ShuffleList(listToShuffle):
    #Loop som lägger till ett slumpmässigt tal lika många gånger som den körs
    for i in range(10000):
        listToShuffle.append(random.randint(0,9))

arrayToSort = []
ShuffleList(arrayToSort)
print(CountingSort(arrayToSort))