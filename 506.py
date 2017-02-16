import sys
sys.setrecursionlimit(10**6)

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
	assert sum(digits) == n
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

mu0 = 189274

none_have_it_lt, all_have_it_gte = ns_categorized(mu0)

print none_have_it_lt, all_have_it_gte

for n in xrange(1, none_have_it_lt):
	assert mu(n) < mu0

for n in xrange(all_have_it_gte, all_have_it_gte + 500):
	assert mu(n) >= mu0

def sum_up_to(nmax):
	for k in count(1):
		none_have_it_lt, all_have_it_gte = ns_categorized(k)
		if nmax >= all_have_it_gte:
			batches_left = (nmax - all_have_it_gte + 1) / 15
			sum_of_this_k = batches_left * slds[k % 6]
			print k, sum_of_this_k
		else:
			break

sum_up_to(3 * 15)

