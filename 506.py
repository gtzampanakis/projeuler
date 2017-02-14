from itertools import *

phi = [0,1,2,3,4,0,3,5,3,0,4,3,2,1,0]
psi = [1,1,1,1,2,3,2,4,3,4,5,5,5,5,6]

def a(n):
	return phi[(n-1)%15]

def mu(n):
	return (
			psi[(n-1)%15]
		+	((n-1)/15) * 6
	)

def c(i):
	assert 0 <= i <= 5
	for ni, n in enumerate(cycle([1,2,3,4,3,2])):
		if ni >= i:
			yield n

def nu(n):
	it = c(a(n))
	mikos = mu(n)
	digits = []
	for digit in it:
		digits.append(digit)
		if len(digits) == mikos:
			break
	return sum(
			d*10**e for d,e in zip(reversed(digits), count())
	)

Scache = {
		1: 1
}

def S(n):
	if n in Scache:
		return Scache[n]
	result = S(n-1) + nu(n)
	Scache[n] = result
	return result

for x in xrange(1, 50):
	x = 10**x
	Sx = S(x)
	print x, Sx % 123454321
