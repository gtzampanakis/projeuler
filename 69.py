from itertools import *

from sieve import *
from prime import *
from pmemoize import *

from pprint import pprint

END = 1000 * 1000

factors = []

def prod(s):
	r = 1
	for si in s:
		r *= si
	return r

for c in xrange(END+1):
	factors.append([])

for p in gen_primes():
	# print p
	if p > END/2:
		break
	for c in xrange(p, END+1, p):
		factors[c].append(p)

maxx = -1
argmax = -1
for n in xrange(2, END+1):
	c = 0
	fs = factors[n]
	if len(fs) <= 1:
		continue
	target_c = n - 1 - n/float(maxx)
	skipn = False
	for l in xrange(1, len(fs)+1):
		for comb in combinations(fs, l):
			c += (
					((n-1)/prod(comb))*(-1)**(l+1)
			)
		if l == 1 and n > 10 and c <= target_c:
			skipn = True
			break
	if skipn:
		continue
	phi = (n-1)-c
	q = n/float(phi)
	if q > maxx:
		maxx = q
		argmax = n
	# print n, phi, q

print maxx
print argmax

