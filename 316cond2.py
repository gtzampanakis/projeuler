import collections, itertools
from memoize import MemoizedFunction

# OVERLAP = 1

@MemoizedFunction
def exp(d, v):

	sum_up_to = collections.defaultdict(float)

	@MemoizedFunction
	def p(a):
		if a < 1:
			result = 0.
		elif a <= d-v:
			result = 10 ** (-d)
		else:

			### result = (
			### 		+ p(a-1)
			### 		- 10**(-d) * p(a-1-d+1)
			### 		+ 10**(1-2*d) * p(a-1-d-2+1)
			### 		+ 10**(2-2*d) * p(a-1-d-1+1)
			### 		- 10**(2-2*d) * p(a-1-d-1)
			### )

			### result = (
			### 		+ 10**(-d) 
			### 		- 10**(-d) * sum_up_to[a-d] 
			### 		- 10**(1-2*d) + 10**(1-2*d) * sum_up_to[a-d-2] 
			### 		+ 10**(2-2*d) * p(a-d-1)
			### )

			result = 10**(-d) * (
					+ 1.
					- sum_up_to[a-d]
					+ (1 if v > 0 else 0) * (
						- 10**(v-d)
						+ 10**(v-d) * sum_up_to[a-2*d+v]
						+ 10**(2*v-d) * p(a-2*d-2*v)
					)
			)


		sum_up_to[a] = sum_up_to.get(a-1, 0) + result

		return result


	exp = 0.
	for a in itertools.count(1):
		pa = p(a)

		if pa < 5.8e-13:
			break

		exp += pa * a

		if 0 and a % 1000 == 0:
			print a, pa, exp

	return int(round(exp, 0))

def n_to_dv(n):
	digits = str(n)
	d = len(digits)

	v = 0
	for length in xrange(1, d/2 + 1):
		if digits[:length] == digits[-length:]:
			v = length

	return d, v


tot = 0
for i in reversed(xrange(2, 1000)):
	n = 10**6 / i
	d,v = n_to_dv(n)
	print i, n,
	expn = exp(d,v)
	tot += expn
	print expn, tot

print tot



	


