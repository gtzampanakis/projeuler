import random
from sieve import *

def is_prime(n):
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True

def prime_factors(n):
	factors = []
	for p in gen_primes():
		while True:
			if n%p == 0:
				factors.append(p)
				n /= p
				if n == 1:
					return factors
			else:
				break
 
_mrpt_num_trials = 5 # number of bases to test
 
def is_probable_prime(n):
	"""
	Miller-Rabin primality test.
 
	A return value of False means n is certainly not prime. A return value of
	True means n is very likely a prime.
 
	>>> is_probable_prime(1)
	Traceback (most recent call last):
		...
	AssertionError
	>>> is_probable_prime(2)
	True
	>>> is_probable_prime(3)
	True
	>>> is_probable_prime(4)
	False
	>>> is_probable_prime(5)
	True
	>>> is_probable_prime(123456789)
	False
 
	>>> primes_under_1000 = [i for i in range(2, 1000) if is_probable_prime(i)]
	>>> len(primes_under_1000)
	168
	>>> primes_under_1000[-10:]
	[937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
 
	>>> is_probable_prime(6438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
	True
 
	>>> is_probable_prime(7438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
	False
	"""
	assert n >= 2
	# special case 2
	if n == 2:
		return True
	# ensure n is odd
	if n % 2 == 0:
		return False
	# write n-1 as 2**s * d
	# repeatedly try to divide n-1 by 2
	s = 0
	d = n-1
	while True:
		quotient, remainder = divmod(d, 2)
		if remainder == 1:
			break
		s += 1
		d = quotient
	assert(2**s * d == n-1)
 
	# test the base a to see whether it is a witness for the compositeness of n
	def try_composite(a):
		if pow(a, d, n) == 1:
			return False
		for i in range(s):
			if pow(a, 2**i * d, n) == n-1:
				return False
		return True # n is definitely composite
 
	for i in range(_mrpt_num_trials):
		a = random.randrange(2, n)
		if try_composite(a):
			return False
 
	return True # no base tested showed n as composite

PRIMES = [2, 3]
def prime(i):
    if i < len(PRIMES):
        return PRIMES[i]
    c = PRIMES[-1] + 2
    while 1:
        found_divisor = False
        stop_point = c**.5
        for p in PRIMES:
            if p > stop_point:
                break
            if c % p == 0:
                found_divisor = True
                break
        if not found_divisor:
            PRIMES.append(c)
            return c
        else:
            c += 2
