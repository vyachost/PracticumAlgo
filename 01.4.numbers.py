## Finding count of prime numbers in the range of (1 : maxNumber)

from datetime import datetime
from numpy import sqrt

maxNumber = 300000
primeList = []

def isPrime(x: int) -> bool:
    for i in primeList:
        if x % i == 0: return False
    return True

def isPrime4(x: int) -> bool:
    j = 2
    while j*j < x+1:
        if (x % j == 0): return False
        j += 1
    return True

time1 = datetime.now()
count = 0
for i in range(2, maxNumber): 
    if isPrime4(i): count += 1
time2 = datetime.now()
deltatime1 = time2 - time1
print('Count1:', count, 'Time is:', deltatime1)

time1 = datetime.now()
count = 0
for i in range(2, maxNumber): 
    if isPrime(i): primeList.append(i)
time2 = datetime.now()
deltatime1 = time2 - time1
print('Count1:', len(primeList), 'Time is:', deltatime1)
