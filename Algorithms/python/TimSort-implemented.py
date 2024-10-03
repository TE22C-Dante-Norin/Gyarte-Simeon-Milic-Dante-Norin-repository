import time
start_time = time.time()
import random

numbers = 100000
listToSort = []

for i in range(numbers):
    listToSort.append(random.randint(0,100000))
listToSort.sort()
print("Process finished --- %s seconds ---" % (time.time() - start_time))