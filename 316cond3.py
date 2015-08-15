import collections, itertools
from memoize import MemoizedFunction

def n_to_vs(n):
	digits = str(n)
	d = len(digits)

	vs = set()

	for i in xrange(1, d):
		if digits[:i] == digits[-i:]:
			vs.add(i)

	return vs
n_to_vs = MemoizedFunction(n_to_vs, int(10e4))

sum_up_to = collections.defaultdict(float)

def prob(n, a):
	d = len(str(n))

	if a < 1:
		result = 0.
	elif a == 1:
		result = 10**(-d)

	else:
		vs = n_to_vs(n)

		result = (
				10**(-d) * (1. - sum_up_to[(n, a-d)])
				- sum(
					prob(n, a-d+v) * 10**(v-d)
					for v in xrange(1, d)
					if v in vs
				)
		)

	sum_up_to[(n, a)] = sum_up_to[(n, a-1)] + result

	key_to_del = (n, a-10000)
	if key_to_del in sum_up_to:
		del sum_up_to[key_to_del]

	return result
prob = MemoizedFunction(prob, int(1e6))

def pw(n, a):
	return prob(rn(n), a)
pw = MemoizedFunction(pw, int(1e6))

ALL_DIGITS = list(reversed([str(d) for d in xrange(0, 10)]))

def rn(n):
	digits = str(n)

	mapping = { }

	for d in digits:
		if d not in mapping:
			mapping[d] = ALL_DIGITS[len(mapping)]

	output = ''.join( mapping[d] for d in digits )

	return int(output)
rn = MemoizedFunction(rn, int(1e6))

def exp(n):
	s = 0.
	for a in itertools.count(1):
		pa = pw(n, a)

		if pa < 5.8e-17:
			break

		inc = pa * a

		### if pa < 1e-10 and inc < .01:
		### 	break

		s += inc

		if 1 and a % 50000 == 0:
			print '***', n, a, pa, s

	return round(s, 0)
exp = MemoizedFunction(exp, int(1e6))

@MemoizedFunction
def prob2(n, a):

	d = len(str(n))

	if a < 1:
		return 0.
	elif a == 1:
		return 10**(-d)

	return prob2(n, a-1) - 10**(-d) * prob2(n, a-d)

@MemoizedFunction
def prob3(n, a):

	d = len(str(n))

	if a < 1:
		return 0.
	elif a == 1:
		return 10**(-d)

	if 1:
		result = (
				+ prob3(n, a-1)
				- 10**(-d) * ( prob3(n, a-d) )
				+ sum( 10**(i-d) * ( prob3(n, a-1-d+i) - prob3(n, a-d+i) ) for i in n_to_vs(n) )
		)

	return result


def expw(n):
	return exp(rn(n))

@MemoizedFunction
def exp5(n):
	d = len(str(n))

	vs = n_to_vs(n)

	result = (
			10**d + 1 -d
			+ sum( 10**i for i in vs )
	)

	return result

print exp5(535)

## print sum(a*prob3(535 ,a) for a in xrange(1, 50000))
# print sum(a*prob2(9 ,a-1) for a in xrange(2, 100000))

if 0:
	print 12312, expw(12312)
	print 123412, expw(123412)
	print 1234512, expw(1234512)
	print 12345612, expw(12345612)

if 1:
	tot = 0
	for i in xrange(2, 1000000):
		n = 10**16 / i
		expn = exp5(rn(n))
		tot += expn
		#print i, n, expn, tot

	print tot
