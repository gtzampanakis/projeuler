import sys
from itertools import *

import pmemoize
from sieve import *

@pmemoize.MemoizedFunction
def isp(n):
	if n <= 1:
		return False
	for ni in xrange(2, int(n**.5)+1):
		if n%ni == 0:
			return False
	return True

def dlc(dl):
	ldl = len(dl)
	return sum(d*10**(ldl-di-1) for di, d in enumerate(copy))

ps = set()
for p in gen_primes():
	sp = tuple(int(d) for d in str(p))
	ps.add(sp)
	l = len(sp)
	inds = range(l)
	for r in xrange(1, l):
		for c in combinations(inds, r):
			primes_found = []
			copy = list(sp)
			for nd in xrange(1 if 0 in c else 0, 10):
				for i in c:
					copy[i] = nd
				tcopy = tuple(copy)
				if tcopy in ps:
					primes_found.append(tcopy)
			if len(primes_found) == 8:
				print p, c, primes_found
				sys.exit()



