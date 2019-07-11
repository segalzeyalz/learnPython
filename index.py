import random

def checkEven(num):
    return num%2==0

for i in range(0,200):
    x = random.randint(0, 200)
    if checkEven(x):
        print(x, " is even")
    else:
        print(x, "is odd")
