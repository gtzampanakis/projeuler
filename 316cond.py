from memoize import MemoizedFunction

# OVERLAP = 1

d = 3

TEN_MINUS_D = 10 ** (-d)

sum_up_to = { }

@MemoizedFunction
def p(a):
	if a < 1:
		result = 0.
	elif a == 1:
		result = TEN_MINUS_D
	elif a == 2:
		result = TEN_MINUS_D
	else:

		def G(i):
			if i == a-d:
				return 0.
			elif i == a-d-1:
				return 10**(2-d)
			else:
				return 10**(1-d)

		paren = (	1 
					### - sum(p(ai) for ai in xrange(1, a-d+1)) 
					- ( sum_up_to.get(a-d, 0) )
					- 10**(1-d) 
					### + sum(G(i) * p(i) for i in xrange(1, a-d+1))
					+ (10**(1-d) * sum_up_to.get(a-d-2, 0) + 10**(2-d) * p(a-d-1))
		)

		result = TEN_MINUS_D * paren

	sum_up_to[a] = sum_up_to.get(a-1, 0) + result

	return result


exp = 0.
for a in xrange(1,1000000):
	pa = p(a)

	if pa < 5.8e-17:
		break

	exp += pa * a

	if a % 1000 == 0:
		print a, pa, exp

print a, pa, exp


