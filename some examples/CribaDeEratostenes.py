from math import sqrt
import numpy as np
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
		
N = raw_input('cuantos primos desea calcular?: ')
N = int(N)
primes = FindPrimes(N)

i = 0
for i in np.arange(100):
		print repr(primes[ 10 * i ]).rjust(5), repr(primes[10 * i + 1 ]).rjust(5), repr(primes[10 * i + 2]).rjust(5), repr(primes[10 * i + 3 ]).rjust(5), repr(primes[10 * i + 4]).rjust(5), repr(primes[10 * i + 5]).rjust(5), repr(primes[10 * i + 6]).rjust(5), repr(primes[10 * i + 7]).rjust(5), repr(primes[10 * i + 8]).rjust(5), repr(primes[10 * i + 9]).rjust(5)
		print


