import numpy as np

from math import sqrt, log

def FindPrimes(limit):
    isPrime = {}
    isPrime[1] = False
    for i in range(2, limit + 1):
        isPrime[i] = True
        checkLimit = int(sqrt(limit)) + 1
    for i in range(2, checkLimit):
        if isPrime[i]:
            for factor in range(2, limit + 1):
                j = i * factor
                if (j > limit): break
                isPrime[j] = False
    primes = []
    for i in range(1, limit + 1):
        if isPrime[i]:
            primes.append(i)
    return np.array(primes)


N = raw_input('Hasta que primo donde desea sumar? ')
N = int(N)
primes = FindPrimes(N)

sum = 0.0
n = 0

print "n".center(3), "sum".center(17), "sum/n".center(18)

for i in primes:

    #print primes

    sum = sum + log(i)

    n = n + 1

    print repr(n). rjust(3), repr(sum).rjust(18), repr(sum/i).rjust(21)




