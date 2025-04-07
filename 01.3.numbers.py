## Finding count of prime numbers in the range of (1 : maxNumber)
from datetime import datetime
from numpy import sqrt

maxNumber = 20000

def isPrime(x: int) -> bool:
    d, j = 0, 1
    while j <= x:
        if (x % j == 0): d += 1
        j +=1
    return d == 2

def isPrime2(x: int) -> bool:
    j = 2
    while j < x:
        if (x % j == 0): return False
        j += 1
    return True

def isPrime3(x: int) -> bool:
    j = 2
    while j < int(sqrt(x))+1:
        if (x % j == 0): return False
        j += 1
    return True

def isPrime4(x: int) -> bool:
    j = 2
    while j*j < x+1:
        if (x % j == 0): return False
        j += 1
    return True


# time1 = datetime.now()
# count = 0
# for i in range(2, maxNumber): 
#     if isPrime(i): count += 1
# time2 = datetime.now()
# deltatime1 = time2 - time1
# print('Count1:', count, 'Time is:', deltatime1)

time1 = datetime.now()
count = 0
for i in range(2, maxNumber): 
    if isPrime2(i): count += 1
time2 = datetime.now()
deltatime1 = time2 - time1
print('Count1:', count, 'Time is:', deltatime1)

time1 = datetime.now()
count = 0
for i in range(2, maxNumber): 
    if isPrime3(i): count += 1
time2 = datetime.now()
deltatime1 = time2 - time1
print('Count1:', count, 'Time is:', deltatime1)

time1 = datetime.now()
count = 0
for i in range(2, maxNumber): 
    if isPrime4(i): count += 1
time2 = datetime.now()
deltatime1 = time2 - time1
print('Count1:', count, 'Time is:', deltatime1)
