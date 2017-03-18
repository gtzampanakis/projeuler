from pprint import pprint
from collections import defaultdict
from sieve import *

def ar(n, d):
	""" Returns the not allowed remainder for each divider. """

	assert d <= n

	strn = str(n)
	r = len(strn)

	m = n%d

	assert m != 0

	mods = [(10**e)%d for e in xrange(1, d)]

	wrong_mod = d-m

	if wrong_mod in mods:
		return mods[mods.index(wrong_mod) - r]
	else:
		return None

ns = [3, 7, 109, 673]

dis = defaultdict(list)
for n in ns:
	for p in gen_primes():
		if p > 1500 or p >= n:
			break
		arnp = ar(n,p)
		if arnp:
			dis[p].append(ar(n,p))

pprint(dict(dis))

valids = 0
total = 0
for i in gen_primes():
	if i > 250:
		break
	for p, mods in dis.iteritems():
		if i%p in mods:
			print i, 'is not allowed'
			break
	else:
		valids += 1
		print i
	total += 1

print 'alloweds:', float(valids)/total*100, '%'

