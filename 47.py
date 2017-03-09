from itertools import *

import pmemoize
from sieve import *

K = 4

ps = set()

@pmemoize.MemoizedFunction
def do(n):

	if n != 1:
		for c in xrange(2, int(n**.5) + 1):
			if n % c == 0:
				break
		else:
			ps.add(n)

	if n == 1:
		result = []
	else:
		for p in ps:
			if n % p == 0:
				result = [p] + do(n/p)
				break
		else:
			result = [n]

	return result

hask = []

for n in count(2):
	nf = len(set(do(n)))
	if nf == K:
		hask.append(n)
		if len(hask) == K:
			break
	else:
		hask = []

print hask
