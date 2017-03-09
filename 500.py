import sys
from itertools import *
from more_itertools import *

from sieve import *

import pmemoize

D = 500500507

def prod(s):
	r = 1
	for x in s:
		r *= x
	return r

def fastmod(s):
	r = len(s)/2

	if r<=1:
		return prod(s) % D

	a,b = s[:r], s[r:]
	return (fastmod(a) * fastmod(b))%D

r = [2,3,4]
N = len(r)

MK = 4

gens = []
for _ in xrange(MK+1):
	gens.append(peekable(gen_primes()))

@pmemoize.MemoizedFunction
def pow2(k):
	return 2**k

N = 500 * 1000 + 500

ns = []
for _ in xrange(N):
	cands = []
	raws = []
	minv = None
	mink = None
	for k in xrange(MK+1):
		p = gens[k].peek()
		v = p**(pow2(k))
		if minv is None or v < minv:
			minv = v
			mink = k
	ns.append(minv)
	gens[mink].next()

print len(ns)

if 0:
	ds = set()
	for rlen in xrange(0, N+1):
		for comb in combinations(ns, rlen):
			ds.add(prod(comb))
	print len(ds)

print fastmod(ns)
