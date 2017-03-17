from collections import *
from itertools import *

dd = defaultdict(list)

def nd(n):
	ds = str(n)
	dist = [0] * 10
	for d in ds:
		dist[int(d)] += 1
	return tuple(dist)

def dist2max(dist):
	themax = []
	for d, freq in enumerate(dist):
		for _ in xrange(freq):
			themax.append(d)
	return int(''.join(str(d) for d in reversed(themax)))

for n in count(1):
	n3 = n**3
	dist = nd(n3)
	perms = dd[dist]
	perms.append(n)
	l = len(perms)
	if l == 5:
		print min(perms)**3
		break
