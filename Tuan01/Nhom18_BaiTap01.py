import math

def printDivisors(n):
    list = []
    i = 1
    while (i < math.sqrt(n)+1):
        if (n % i == 0):
            if (n / i == i):
                list.append(int(i))
            else:
                print(i, end = " ")
                list.append(int(n / i))
        i+=1

    for i in list[::-1]:
        print(i, end = " ")

printDivisors(100)