from itertools import *

from sieve import *
from prime import *
from pmemoize import *

from pprint import pprint

END = 10 * 1000 * 1000

factors = []

def prod(s):
	r = 1
	for si in s:
		r *= si
	return r

def digits(a):
	return sorted(str(a))

for c in xrange(END+1):
	factors.append([])

for p in gen_primes():
	# print p
	if p > END/2:
		break
	for c in xrange(p, END+1, p):
		factors[c].append(p)

minx = 10e50
argmax = -1
for n in xrange(2, END+1):
	c = 0
	fs = factors[n]
	if len(fs) > 2:
		continue
	for l in xrange(1, len(fs)+1):
		for comb in combinations(fs, l):
			c += (
					((n-1)/prod(comb))*(-1)**(l+1)
			)
	phi = (n-1)-c
	q = n/float(phi)
	if digits(n) == digits(phi):
		if q < minx:
			minx = q
			argmax = n
		print n, phi, fs, q

print minx
print argmax

