import sys
import lib

primes_encountered = set()
i = 1
while True:
	i += 1
	isprime = lib.isprime(i)
	if isprime:
		primes_encountered.add(i)
	if not isprime and i % 2 == 1:
		found_hit = False
		for pr in primes_encountered:
			diff = i - pr
			if diff % 2 == 0:
				possible_sq = diff / 2
				if possible_sq in list(x**2 for x in xrange(1, possible_sq+1)):
					found_hit = True
					break
		if not found_hit:
			print i 
			break
