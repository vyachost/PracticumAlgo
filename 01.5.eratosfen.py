import numpy as np
import datetime

start = datetime.datetime.now()

maxNum = 1000000

number = np.zeros(maxNum+1)
numbers = [i for i in range(maxNum+1)]

number[0] = True
number[1] = True
for j in range(2, maxNum):
    if not number[j]:
        k = j
        while k*k <= maxNum:
            for i in range(k*k, maxNum+1, k): number[i] = True
            k +=1

prime = list([numbers[i] for i in range(maxNum) if not number[i]])

print(len(prime))
finish = datetime.datetime.now()
print('Time:', finish-start)