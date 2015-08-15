import itertools
import memoize

digits = 6

sum_per_k = { }
for di in xrange(1, 1 + digits):
	sum_per_k[di] = 1.

@memoize.MemoizedFunction
def p(k):
	if k > digits:
		sum_per_k[k] = sum_per_k[k-1] - p(k-digits)
	return 10**(-digits) * (sum_per_k[k])
	

running = 0.

for a in itertools.count(1):
	pa = p(a)
	running += a * pa
	if a % 2000 == 0:
		print a, pa, running


