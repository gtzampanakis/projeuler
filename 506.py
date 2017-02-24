import sys, math
import pmemoize

from itertools import *

phi = [0,1,2,3,4,0,3,5,3,0,4,3,2,1,0]
psi = [1,1,1,1,2,3,2,4,3,4,5,5,5,5,6]

MOD = 123454321

def log2(x):
	return int(math.log(x, 2))

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

offset = 10
for n in xrange(1 + offset, 66 * 15 + 1 + offset, 15):
	print '{n:>10d}   {nun:>110d}'.format(n = n, nun = nu(n))
	if 0:
		if n % 15 == 0:
			print

M = 4232097
m = 260517

b = 2 ** 6

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
def mod(x):
	return x%MOD

@pmemoize.MemoizedFunction
def fastmod(exp):
	if exp == 1:
		return 10 % MOD
	else:
		l = exp/2
		r = exp-l
		return (fastmod(l) * fastmod(r)) % MOD
	

@pmemoize.MemoizedFunction
def CC(N):
	if N == 0:
		result = 0
	elif N == 1:
		result = M
	else:
		assert 2**log2(N) == N
		HN = N/2
		A = CC(HN)
		result = (2*A)%MOD + ((2*A)%MOD * fastmod(6 * HN))
	return result

@pmemoize.MemoizedFunction
def Sb3(N):
	""" Powers of 2. """
	assert 2**log2(N) == N
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
print

@pmemoize.MemoizedFunction
def CC2(width):
	if width == 0:
		return 0
	assert width % 6 == 0
	if width == 6:
		return M
	return ((M%MOD) * ((10**(width-6)))%MOD) + ((CC2(width-6))%MOD)

def strat(nu):
	nuin = nu
	ss = []
	offs = []
	bs = []
	b = 0
	off = 0
	while True:
		b = nu/15
		if b == 0:
			break
		b = 2**log2(b)
		nu -= b * 15
		s = Sb3(b)
		ss.append(s)
		offs.append(off)
		bs.append(b)
		off += mu(b * 15)

	tot = 0
	for ssi, offi, bi in zip(ss, offs, bs):
		print bi*15, bi, offi, ssi
		assert offi % 6 == 0
		tot += (
			ssi * (10**offi) + CC2(offi)*bi
		)

	print 'remainder:', nuin - sum(bs)*15
	return tot

# print CC2(6)
# print CC2(6)
# print CC2(6)
# print CC2(12)
# print CC2(24)

x = 66 * 15

print strat(x) % MOD
print S(x) % MOD

@pmemoize.MemoizedFunction
def nsix(s, n):
	if n == 0:
		result = 0
	elif n == 1:
		result = s
	else:
		l = n/2
		r = n-l
		result = (
			mod(nsix(s,l)) * fastmod(6*r) + mod(nsix(s,r))
		)
	return result

@pmemoize.MemoizedFunction
def DD(rn,o):
	if rn == 1:
		result = 0
	else:
		result = 0
		sextet = nu(15+o+1) % 10**6
		nsextets = rn-1
		result = nsix(sextet, nsextets)
	return result

@pmemoize.MemoizedFunction
def BB(r, o):
	assert 0 <= o <= 14
	if r == 1:
		result = nu(r+o)
	else:
		l = r/2
		h = r-l
		result = (
				mod(BB(l,o))
			+ 	mod(BB(h,o)) * fastmod(6*l)
			+   mod(DD(l+1,o)) * mod(h)
		)
	return result

print mod(BB(16,offset))

t = 10**14

tot = 0
for o in xrange(0, 15):
	rn = (t+14-o)/15
	print o, rn, 15*(rn-1)+o+1
	tot += mod(BB(rn, o))

print mod(tot)

