import memoize, sys

PRINT = 0
F = 100

Ts = range(1, 9)
def T(s1, s2):
	ps = [R(s1, s2, 2, T) for T in Ts]
	result = Ts[ps.index(max(ps))]
	print 'T({s1}, {s2}) = {T}'.format(s1=s1, s2=s2, T=result)
	return result

T = memoize.MemoizedFunction(T, 100**3)

def R(s1, s2, u, force_T = None):
	if PRINT: print 'Calling R with parameters: {p}'.format(p = (s1, s2, u))
	assert s1 >= 0 and s2 >= 0
	assert s1 >= F and s2 < F or s1 < F and s2 >= F or s1 < F and s2 < F
	assert u in (2, 1)
	if s1 >= F: result = 0.
	elif s2 >= F: result = 1.
	else:
		if u == 2:
			if force_T is None:
				T_to_use = T(s1, s2)
			else:
				T_to_use = force_T
			assert T_to_use in Ts
			A = 2**(T_to_use - 1)
			one_over_2A = 1./(2*A)
			first_term = one_over_2A * R(s1, s2+A, 1)
			second_term = (1-one_over_2A) * (.5) * R(s1+1, s2, 2)
			denom = 1. - .5 * (1 - one_over_2A)
			result = (first_term + second_term) / denom
		elif u == 1:
			result = .5 * (R(s1+1, s2, 2) + R(s1, s2, 2))
	if PRINT: print 'Returning from R: {result}'.format(result=result)
	assert result >= 0. and result <= 1.
	return result

R = memoize.MemoizedFunction(R, F*F*2*10*10)

sys.setrecursionlimit(10000)
print R(0, 0, 1)
	
