import collections, sys
from pprint import pprint
from memoize import MemoizedFunction

@MemoizedFunction
def ds(n):
	return sum( int(c) for c in str(n) )

M = 137

DTK = {
	0: 0,
	1: 0,
	2: 1,
	3: 3,
	4: 3,
	5: 4,
	6: 6,
	7: 6,
	8: 8,
	9: 10,
}

TRIP_TO_CONT_K = { }

@MemoizedFunction
def k_for_addition(a1, a2):
	### div = ( ds(a1) + ds(a2) - ds(a1 + a2) )
	### d = div / 9
	### m = div % 9
	### assert m == 0
	return ( ds(a1) + ds(a2) - ds(a1 + a2) ) / 9

@MemoizedFunction
def n_to_dig(n):
	digits = [ int(c) for c in str(n) ]
	return digits

@MemoizedFunction
def dig_to_n(dig):
	return int(''.join(str(d) for d in dig))

@MemoizedFunction
def prod_ignor_b(n):
	dig = n_to_dig(n)
	if len(dig) == 1:
		return n*M
	return prod_ignor_b(dig_to_n(dig[1:]))/10 + int(dig[0]) * M
	

@MemoizedFunction
def K_for_mult(n):
	digits = [ int(c) for c in str(n) ]
	if len(digits) == 1:
		d = digits[0]
		return DTK[d]
	dig_to_n(digits[1:])
	return (
			+ K_for_mult(n_to_pass) 
			+ DTK[digits[0]] 
			+ k_for_addition(digits[0]*M, prod_ignor_b(n))
	)

A = 0.9

T = collections.defaultdict(int)

T.update({
		(0, ds(0), 0*M/10, K_for_mult(0)) : 1,
		(1, ds(1), 1*M/10, K_for_mult(1)) : 1,
		(1, ds(2), 2*M/10, K_for_mult(2)) : 1,
		(1, ds(3), 3*M/10, K_for_mult(3)) : 1,
		(1, ds(4), 4*M/10, K_for_mult(4)) : 1,
		(1, ds(5), 5*M/10, K_for_mult(5)) : 1,
		(1, ds(6), 6*M/10, K_for_mult(6)) : 1,
		(1, ds(7), 7*M/10, K_for_mult(7)) : 1,
		(1, ds(8), 8*M/10, K_for_mult(8)) : 1,
		(1, ds(9), 9*M/10, K_for_mult(9)) : 1,
})

psi_to_T = { 1: T }

MAX_PSI = 19
EXH = 0

def old_key_to_new_key(old_key, x):
	zold, dold, told, kold = keyold
	d = dold + x
	t = (told + x*M)/10
	k = kold + K_for_mult(x) + k_for_addition(x*M, told)

	key = (1 if x else 0, d, t, k)
	return key

for psi in xrange(2, MAX_PSI):
	T = collections.defaultdict(int)
	Told = psi_to_T[psi-1]

	for x in xrange(0, 10):

		for keyold, count in Told.iteritems():

			key = old_key_to_new_key(keyold, x)

			T[key] += count

	print psi, len(T)
	psi_to_T[psi] = T


## pprint(dict((k,v) for k,v in psi_to_T[MAX_PSI-1].iteritems() if k[0] == 1))

found = 0
for psi in xrange(1, MAX_PSI):
	print psi
	T = psi_to_T[psi]
	for key, count in T.iteritems():
		z, d, t, k = key
		if z and d % 9 == 0:
			# if d == 11*d - 9*k:
			if 10*d == 9*k:
				found += count
print found


if EXH:
	found = 0
	for i in xrange(1, 10**(MAX_PSI-1)):
		if ds(i) == ds(i*137):
			found += 1
	print found


if 0:
	for trip in xrange(0, 1000):
		digits = [ int(c) for c in str(trip).zfill(3) ]
		ks1 = [ DTK[d] for d in digits]
		print digits, ks1
		for mp in xrange(0, 10):
			print trip, trip * M, trip * M / 100


if 0:
	for i in xrange(1, 1000):
		if ds(i) == ds(i*137):
			rest = i % (10**(len(str(i))-1))
			print i, i*137, ds(i), ds(i)*11, ds(i)*11 - ds(i*137)

if 0:
	for n in xrange(1, 6):
		found = 0
		for i in xrange(10**(n-1), 10**n):
			if ds(i) == ds(i*137):
				found += 1
				# print i, i*137, ds(i), ds(i)*11, ds(i)*11 - ds(i*137)
		print n, 10**(n-1), 10**n, found

if 0:
	for start in xrange(0, 10000, 1000):
		ds23 = [ ]
# positions on which ds=23 occurs:
		for i in xrange(start, start + 1000):
			if ds(i) == ds(i*137):
				ds23.append(i)
		print start, len(ds23)
