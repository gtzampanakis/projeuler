import sys
import pmemoize

from itertools import *

phi = [0,1,2,3,4,0,3,5,3,0,4,3,2,1,0]
psi = [1,1,1,1,2,3,2,4,3,4,5,5,5,5,6]

MOD = 123454321

def a(n):
	return phi[(n-1)%15]

def mu(n):
	return (
			psi[(n-1)%15]
		+	((n-1)/15) * 6
	)

def c(i):
	assert 0 <= i <= 5
	for ni, n in enumerate(cycle(['1','2','3','4','3','2'])):
		if ni >= i:
			yield n

nucache = {
}

def nu(n):
	if n in nucache:
		return nucache[n]
	it = c(a(n))
	mikos = mu(n)
	digits = []
	def loop():
		for digit in it:
			digits.append(digit)
			if len(digits) == mikos:
				break
	loop()
	# assert sum(digits) == n
	result = int(''.join((d) for d in (digits)))
	nucache[n] = result
	return result
	# return sum(
	# 		d*10**e for d,e in zip(reversed(digits), count())
	# )

Scache = {
		1: 1
}

def S(n):
	if n in Scache:
		return Scache[n]
	result = S(n-1) + nu(n)
	Scache[n] = result
	return result

def ns_categorized(mu0):

	none_have_it_lt = (15*mu0 - 90) / 6 - 1
	none_have_it_lt = none_have_it_lt / 15 * 15
	if none_have_it_lt <= 0:
		none_have_it_lt = 1

	all_have_it_gte = 15*mu0/6
	all_have_it_gte = all_have_it_gte + (15 - all_have_it_gte % 15) + 1
	if all_have_it_gte <= 0:
		all_have_it_gte = 1

	return none_have_it_lt, all_have_it_gte

lds = []
for n in xrange(99 * 15 + 1, 100 * 15 + 1):
	# print n, str(nu(n))[-6:], str(nu(n))[-12:-6]
	lds.append(str(nu(n))[-6:])

slds = []
for i in reversed(xrange(6)):
	tot = 0
	for ld in lds:
		tot += int(ld[i])
	slds.append(tot)

def sum_up_to(nmax):
	assert nmax % 15 == 0
	ss = []
	for k in count(1):
		sum_of_this_k = 0
		none_have_it_lt, all_have_it_gte = ns_categorized(k)
		batches_left = (nmax - all_have_it_gte + 1) / 15
		if batches_left >= 0:
			sum_of_this_k += batches_left * slds[(k-1) % 6]
		def loop2(sum_of_this_k_in):
			for n in xrange(none_have_it_lt, all_have_it_gte):
				if n > nmax:
					break
				if mu(n) >= k:
					while mu(n-15) >= k:
						n = n - 15
					sum_of_this_k_in += int(str(nu(n))[-k])
			return sum_of_this_k_in
		sum_of_this_k = loop2(sum_of_this_k)
		if sum_of_this_k == 0:
			break
		ss.append(sum_of_this_k)
	return ss

for n in xrange(1, 6 * 15 + 1):
	print '{n:>10d}   {nun:>100d}'.format(n = n, nun = nu(n))
	if n % 15 == 0:
		print

M = 4232097
m = 260517

b = 2 ** 10

def Sb(b):
	s = 0
	for i in xrange(1, b+1):
		s += ( M * (b-i) + m ) * 10**((i-1)*6)
	return s

def Sb2(b):
	assert b >= 1
	if b == 1:
		return Sb(b)
	assert b >= 2
	return (
		Sb(b-1) +
		m * 10**(6*(b-1)) +
		M * sum(10**(6*(i-1)) for i in xrange(1, b))
	)

r1 = Sb(b) % MOD
r2 = Sb2(b) % MOD
assert r1 == r2

@pmemoize.MemoizedFunction
def fastmod(exp):
	if exp < 10:
		result = 10**exp%MOD
	else:
		result = 10**10%MOD
		for _ in xrange(10, exp):
			result = (10*result) % MOD
	return result

@pmemoize.MemoizedFunction
def CC(N):
	if N == 1:
		result = M
	else:
		HN = N/2
		A = CC(HN)
		result = (2*A)%MOD + ((2*A)%MOD * fastmod(6 * HN))
	return result

@pmemoize.MemoizedFunction
def Sb3(N):
	""" Powers of 2. """
	if N == 1:
		result = Sb(1)
	else:
		HN = N/2
		A  = Sb3(HN)
		low = A
		high = (A%MOD * fastmod(6 * HN)) + (CC(HN))%MOD
		result = (low + high)
	return result

r3 = Sb3(b) % MOD

assert r2 == r3

print r3 % MOD

