import itertools, collections
import memoize
import scipy as s
from lib import denominations_count_only, denominations_flat

M = 250250

def lk(n, l):
	s = str(n)[-l:]
	return int(s)

def l3(n):
	return lk(n, 3)

def l1(n):
	return lk(n, 1)

def is_bp(n):
	return l3(n**2) == l3(n)

bps = set(n for n in xrange(0, 1000) if is_bp(n))

def per(n):
	if n >= 1000:
		return per(l3(n))
	c = 1
	for i in itertools.count(1):
		c = l3(c * n)
		if c in bps:
			return i

per = memoize.MemoizedFunction(per, M)
periods = [None, None] + [per(i) for i in xrange(2, M+1)]

def slow_power(n, k):
	assert n > 0 and k > 0
	return l3(n ** k)

def fast_power(n, k):
	if n == 0:
		return 0
	assert n > 0 and k > 0
	if n == 1:
		return n
	if n >= 1000:
		return fast_power(l3(n), k)
	period = periods[n]
	r = k % period
	at_period = n ** period
	result = at_period * l3(n ** r)
	return l3(result)

def subsets(l):
	return itertools.chain(
		*(itertools.combinations(l, n) for n in xrange(1, len(l)+1))
	)

fast_power = memoize.MemoizedFunction(fast_power, M)
	
A = [fast_power(k, k) for k in xrange(1, M+1)]
Ad = sorted(set(A))

final_digit_to_Ad_el = collections.defaultdict(list)
for n in Ad:
	key = l1(n)
	final_digit_to_Ad_el[key].append(n)

#ways_to_make_10 = list(denominations_flat(10, range(2,10)))
#
#total = 0
#for way in ways_to_make_10:
#	way = way[-1:] + way[:-1]
#	to_cross_join = [ ]
#	for i, el in zip(itertools.count(1), way):
#		for j in xrange(el):
#			to_cross_join.append(final_digit_to_Ad_el[i])
#	#for s in itertools.product(*to_cross_join):
#	#	total += 1
#	if to_cross_join != [ ]:
#		to_add = 1
#		for l in to_cross_join:
#			to_add *= len(l)
#		total += to_add
#
#print
#print total
#
#for key in (final_digit_to_Ad_el.keys()):
#	print key, len(final_digit_to_Ad_el[key])

sum_Ad = sum(Ad)
for m in xrange(250, sum_Ad+1, 250):
	ways_to_make_m = list(denominations_flat(m, [n for n in Ad if n != 1 and n <= m]))
	print m, len(ways_to_make_m)

