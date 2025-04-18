# the number of numbers where the first digit is equal to the second

def countOfNumbers1():
    c = 0
    for i in range(10, 100):
        a = i//10
        b = i%10
        if a == b: c += 1
    return c

print(countOfNumbers1())

def countOfNumbers2():
    c = 0
    for i in range(1, 10):
        for j in range(1,10):
            if i == j: c += 1
    return c

print(countOfNumbers2())

# number of lucky tickets with a four-digit number
def luckyDigit1():
    x = 0
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10): 
                    if (a+b) == (c+d): x +=1
    return x

print(luckyDigit1())

def luckyDigit2():
    x = 0
    for a in range(0, 10):
        for b in range(0, 10):
            ab = a + b
            for c in range(0, 10):
                d = ab - c
                if (0 <= d <= 9): x +=1
    return x

print(luckyDigit2())

# number of lucky tickets with a six-digit number
def luckyDigit3():
    x = 0
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    for e in range(0, 10): 
                        for f in range(0, 10):
                            if (a+b+c) == (d+e+f): x +=1
    return x

print(luckyDigit3())
